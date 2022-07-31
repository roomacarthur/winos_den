from .models import ContactUs, NewsLetter
from django import forms
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        

class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'

