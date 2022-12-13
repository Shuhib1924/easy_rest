from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET', 'POST'])
def product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data) #das ist der schritt indem offline data vom api aufgenommen wird
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def edit(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist():
        pass
        # return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)