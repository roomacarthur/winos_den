from django.db import models

# Create your models here.
class Reviews(models.Model):
    """
    model for sie visitors to anaonymously submit a review. 
    """

    title = models.CharField(max_length=80, blank=False, null=True)
    product_name = models.CharField(max_length=80, blank=False, null=True)
    body = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
