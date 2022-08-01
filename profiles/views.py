from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from .models import CustomerProfile
from .forms import CustomerProfileForm
from checkout.models import Order

# Create your views here.
def profile(request):
    """
    display customer profile.
    """
    profile = get_object_or_404(CustomerProfile, user=request.user)

    if request.method == "POST":
        form = CustomerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile was successfully updated!")
    form = CustomerProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        'form': form,
        'orders': orders,
    }
    
    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a historic confirmation, for {order_number}, \
          The Original confirmation was sent via email.'
    ))

    template = "checkout/checkout_success.html"
    context = {
        'order': order,
        'form_profile': True,
    }

    return render(request, template, context)