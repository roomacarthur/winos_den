
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'house_name',
            'street_address_1',
            'street_address_2',
            'city',
            'post_code',
            'country',
        )
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Contact Number',
            'house_name': 'House Name/Number',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'city': 'City/Town',
            'post_code': 'Post Code',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}*'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False