from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts.as_view(), name='products'),
    path('<int:pk>', views.ProductDetails.as_view(), name='product_detail'),
    path('under-10/', views.UnderTen.as_view(), name='under-10'),
    path('add_product', views.AddNewProduct.as_view(), name='add_product'),
    path('<int:pk>/edit/', views.EditProduct.as_view(), name='edit_product'),
    path('<int:pk>/delete/', views.DeleteProduct.as_view(), name='delete_product'),
    
]
