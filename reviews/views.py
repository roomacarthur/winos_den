from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from .models import Reviews 
from .forms import ReviewForm
from django.views.generic.edit import CreateView
# Create your views here.
class Reviews(CreateView):

    model = Reviews
    template_name = 'reviews/review.html'
    form_class = ReviewForm

    def get_success_url(self):
        messages.success(self.request, 'Thanks for your review! Sign up to our newsletter to see if you will feature!')
        return reverse('home')