from django.urls import path
from . import views


urlpatterns = [
    path('', views.product, name='product'),
    path('single/<int:pk>', views.edit, name='edit')
]