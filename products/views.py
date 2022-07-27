from django.shortcuts import render
from django.views import generic, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test
from .models import Product, Category
from .forms import ProductForm

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



# @user_passes_test(lambda u: u.is_superuser)
class AddNewProduct(CreateView):
    """
    
    """
    model = Product
    form_class = ProductForm
    template_name = 'products/product_new.html'
    success_url = '/products/'