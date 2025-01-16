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


class ShippingView(TemplateView):
    template_name = 'home/shipping_policy.html'


class FaqView(TemplateView):
    template_name = 'home/faq.html'


class PolicyView(TemplateView):
    template_name = 'home/policies.html'


class ContactUs(CreateView):
    """
    CBV to render contact us form on contact_us.html template,
    upon successful submission prompt user with success message.
    """
    model = ContactUs
    form_class = ContactForm
    template_name = 'home/contact_us.html'

    def get_success_url(self):
        """
        Upon successful submission return to contact remplate
        Prompt user with success message.
        """
        messages.success(
            self.request,
            'Thank you for contacting us! We aim to reply within 24 hours.')
        return reverse('contact_us')


class NewsLetter(CreateView):
    """
    CBV to render newsletter signup form.
    Upon successful signup, prompt user with success message.
    """

    model = NewsLetter
    form_class = NewsLetterForm
    template_name = 'home/subscribe.html'

    def get_success_url(self):
        """
        Upon successful submission return user to homepage.
        Prompt user with success message.
        """
        messages.success(self.request, 'Thanks for Signing Up!')
        return reverse('home')
