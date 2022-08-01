from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField 
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class CustomerProfile(models.Model):
    """
    Customer User Profile. 

    To Store Default info

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_phone_number = models.CharField(max_length=30, blank=False, null=True)
    user_house_name = models.CharField(max_length=50, blank=False, null=True)
    user_street_address_1 = models.CharField(max_length=80, blank=False, null=True)
    user_street_address_2 = models.CharField(max_length=80, blank=True, null=True)
    user_city = models.CharField(max_length=80, blank=False)
    user_post_code = models.CharField(max_length=15, blank=False, null=True)
    user_country = CountryField(blank_label='Country',blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Update or Create customer profiles
    """
    if created:
        CustomerProfile.objects.create(user=instance)
    # Existing customers, save profile.
    instance.customerprofile.save()