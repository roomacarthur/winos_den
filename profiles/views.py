from django.shortcuts import get_object_or_404, render

from .models import CustomerProfile

# Create your views here.
def profile(request):
    """
    display customer profile.
    """
    profile = get_object_or_404(CustomerProfile, user=request.user)
    template = "profiles/profile.html"
    context = {
        'profile': profile,
    }
    
    return render(request, template, context)