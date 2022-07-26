from django.shortcuts import render
from django.views import generic, View
from django.shortcuts import get_object_or_404, render

from .models import Product, Category

# class AllProducts(generic.ListView):
#     """
#     Displays all Products in relation to the model: Product
#     Orders products by Price, Ascending.
#     Renders on products_list.html
#     """
#     model = Product
#     queryset: Product.objects.order_by('-price')
#     template_name = 'product_list.html'

class AllProducts(generic.ListView):
    """
    Displays all items relating to the model: Product.
    Renders on the template product_list.html
    """
    model = Product
    template_name = 'products/product_list.html'

class UnderTen(generic.ListView):
    """
    Displays all items relating to the model: Product.
    Renders on the template product_list.html
    """
    model = Product
    template_name = 'products/under_10.html'



class ProductDetails(generic.DetailView):
    """
    
    """
    model = Product
    pk_url_kwarg = 'id'
    template_name = 'products/product_details.html'