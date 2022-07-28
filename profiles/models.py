from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField 

# Create your models here.

class CustomerProfile(models.Model):
    """
    Customer User Profile. 

    To Store Default Address

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=True)
    house_name = models.CharField(max_length=50, blank=False, null=True)
    street_address_1 = models.CharField(max_length=80, blank=False, null=True)
    street_address_2 = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=False)
    post_code = models.CharField(max_length=15, blank=False, null=True)
    country = CountryField(blank_label='Country',blank=True, null=True)
    
    def __str__(self):
        return self.first_name
    