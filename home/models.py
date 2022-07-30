from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    email = models.EmailField(max_length=80, blank=False, null=True)
    submitted_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=False, null=True)


class NewsLetter(models.Model):
    email = models.EmailField(max_length=80, blank=False, null=True)
    signed_up_on = models.DateTimeField(auto_now_add=True)