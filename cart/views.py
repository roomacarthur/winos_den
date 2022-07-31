from products.models import Product
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import (
    render, redirect, reverse, HttpResponse,
    get_object_or_404
)


def cart_view(request):
    """ A view that renders the bag contents page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)

def update_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})


    cart[item_id] = quantity
    messages.success(
        request,(f'Updated {product.name} '
        f'quantity to {cart[item_id]}')
    )

    request.session['cart'] = cart
    return redirect(reverse('cart'))

def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})
    cart.pop(item_id)
    messages.success(request, f'Removed {product.name} from your bag')
    request.session['cart'] = cart
    return HttpResponse(status=200)
