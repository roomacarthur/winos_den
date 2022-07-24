from django.shortcuts import render
from django.views import generic, View
from django.shortcuts import get_object_or_404, render

from .models import Product, Category

# Create your views here.
def index(request):
    """A view to return the index page."""
    return render(request, 'products/index.html')

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
    
    """
    model = Product
    template_name = 'products/product_list.html'


class ProductDetails(generic.DetailView):
    """
    
    """
    model = Product
    pk_url_kwarg = 'id'
    template_name = 'products/product_details.html'