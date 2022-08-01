from .models import ContactUs, NewsLetter
from django.forms import ModelForm


class ContactForm(ModelForm):
    """
    Render form with all fields from the ContactUs model
    """
    class Meta:
        model = ContactUs
        fields = '__all__'


class NewsLetterForm(ModelForm):
    """
    Render form with only the email field from
    NewsLetter mode.
    """
    class Meta:
        model = NewsLetter
        fields = (
            'email',
            )
