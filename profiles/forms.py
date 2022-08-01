from django import forms
from .models import CustomerProfile

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_phone_number': 'Phone Number',
            'user_house_name': 'House Name/Number',
            'user_street_address_1': 'Street Address 1',
            'user_street_address_2': 'Street Address 2',
            'user_city': 'City/Town',
            'user_post_code': 'Post Code',
            'user_country': 'Country',
        }

        self.fields['user_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'user_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False