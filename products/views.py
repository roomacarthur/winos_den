from django.shortcuts import render
from django.views import generic, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Product, Category
from .forms import ProductForm
from django.contrib import messages
# from django.db.models import Q


class AllProducts(generic.ListView):
    """
    Displays all items relating to the model: Product.
    Renders on the template product_list.html
    """
    model = Product
    template_name = 'products/product_list.html'
    paginate_by = 9
    
    # search parameters 
    def get_queryset(self):
    # if 'q' in self.request.GET:
        query = self.request.GET.get('q')
        if query:
            # if value searched matches name or description return items.
            object_list = self.model.objects.filter(name__icontains=query)|self.model.objects.filter(description__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list
        



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
    # pk_url_kwarg = 'id'
    template_name = 'products/product_details.html'


class AddNewProduct(CreateView, UserPassesTestMixin, LoginRequiredMixin):
    """
    A view to provide a form for user to create new product.
    Check to ensure user is superuser. 
    Build form from the Product model.
    Render on product_new.html
    upon success return to products list.
    """
    def test_func(self):
        return self.request.user.is_superuser

    model = Product
    form_class = ProductForm
    template_name = 'products/product_new.html'
    success_url = '/products/'


class EditProduct(UpdateView, UserPassesTestMixin, LoginRequiredMixin):

    def test_func(self):
        return self.request.user.is_superuser

    model = Product
    form_class = ProductForm
    template_name = "products/product_edit.html"

    def get_success_url(self):
        """
        Upon successful update return user to original products page. 
        Prompt user with success message that includes product name.
        """
        name = self.object.name
        messages.success(self.request, f'{name}, was updated successfully.')
        pk = self.kwargs['pk']
        return reverse('product_detail',kwargs={'pk':pk})


class DeleteProduct(DeleteView, UserPassesTestMixin, LoginRequiredMixin):

    def test_func(self):
        return self.request.user.is_superuser

    model = Product
    template_name = 'products/product_delete.html'
    success_message = 'Product successfully deleted.'
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)

    def get_success_url(self):
        return reverse('products')
    
    def delete(self, request, *args, **kwargs):
        """
        Success message to be displayed after deletion of post.
        """
        messages.success(self.request, self.success_message)
        return super(DeleteProduct, self).delete(request, *args, **kwargs)