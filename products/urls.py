from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts.as_view(), name='products'),
    path('<int:id>', views.ProductDetails.as_view(), name='product_detail'),
    path('under-10/', views.UnderTen.as_view(), name='under-10'),
    path('add_product', views.AddNewProduct.as_view(), name='add_product'),
]
