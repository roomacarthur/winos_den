from .models import ContactUs, NewsLetter
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        

class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = (
            'email',
            )