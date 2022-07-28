from django.views.generic import TemplateView
from django.shortcuts import render, redirect

class CartView(TemplateView):
    """
    A view to return the index page, rendered on the index.html template.
    """
    template_name = 'cart/cart.html'

def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)