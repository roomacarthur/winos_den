from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Model to 
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    display_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)


    def __str__(self):
        return self.name