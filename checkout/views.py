from django.conf import settings
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from cart.contexts import cart_contents

from .models import Order, OrderLineItem
from .forms import OrderForm
from products.models import Product

import json
import stripe


@require_POST
def cache_checkout_data(request):
    """
    Cache data to allow for user to save info for later use.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, "Unfortunately, your payment can't be \
            processed right now. Please try again soon.")
        return HttpResponse(content=e, status=400)


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'house_name': request.POST['house_name'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'city': request.POST['city'],
            'post_code': request.POST['post_code'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    isinstance(item_data, int)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your cart no longer exists.")
                    )
                    order.delete()
                    return redirect(reverse('cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number])
                )
        else:
            messages.error(request, 
            'OOPS! Looks like you made a mistake, Please check your information.')
    else:
        cart = request.session.get('cart')
        if not cart:
            messages.error(request, 'Your Cart is Empty')
            return redirect(reverse('products'))

        session_cart = cart_contents(request)
        total = session_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order  = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order { order_number } successfully processed! \
       Email Confirmation has been sent to {order.email}')
    if 'cart' in request.session:
        del request.session['cart']
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)