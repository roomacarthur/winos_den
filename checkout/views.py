from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import OrderForm
# Create your views here.

def checkout(request):
    cart = request.session.get('cart')
    if not cart:
        messages.error(request, 'Your Cart is Empty')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LROGwId8ivfQUMkfbgaIW2HTI2vQGueHAxJb2qcDWjo3MOop5Op64Kp4IOThagti1TIpsqmi1b891FxZ09dXw220034jqgbPq',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)