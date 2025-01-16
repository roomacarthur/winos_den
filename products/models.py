from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    Model to store different categories within the DB.
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    display_name = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.CharField(max_length=160, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Region(models.Model):
    """
    Model to store different regions within the DB.
    """
    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to='regions/', null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    display_name = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.CharField(max_length=160, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model to store products in the DB.
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL, related_name="products")
    region = models.ForeignKey(
        'Region', null=True, blank=True, on_delete=models.SET_NULL, related_name="products")
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=160, null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    abv = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/product/{self.slug}/"

    def reduce_stock(self, quantity):
        """Reduce stock by a given quantity."""
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
        else:
            raise ValueError("Insufficient stock")
