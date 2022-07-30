from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import NewsLetterForm, ContactForm
from .models import ContactUs, NewsLetter
from django.urls import reverse
from django.contrib import messages

class IndexView(TemplateView):
    """
    A view to return the index page, rendered on the index.html template.
    """
    template_name = 'home/index.html'

# def contact_us():
#     #as

class ContactUs(CreateView):

    model = ContactUs
    form_class = ContactForm
    template_name = 'home/contact_us.html'

    def get_success_url(self):
        """
        Upon successful submission return user to 
        Prompt user with success message that includes product name.
        """
        messages.success(self.request, 'Thank you for contacting us! We aim to reply within 24 hours.')
        return reverse('contact_us')

class NewsLetter(CreateView):

    model = NewsLetter
    form_class = NewsLetterForm

    def get_success_url(self):
        """
        Upon successful submission return user to 
        Prompt user with success message that includes product name.
        """
        messages.success(self.request, 'Thanks for Signing Up!')
        return reverse('contact_us')