from .models import Reviews
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'
        