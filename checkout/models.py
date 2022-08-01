from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from profiles.models import CustomerProfile
from products.models import Product
import uuid


# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    customer_profile = models.ForeignKey(
        CustomerProfile, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='orders'
        )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    house_name = models.CharField(max_length=50, blank=False, null=True)
    street_address_1 = models.CharField(max_length=80, blank=False, null=True)
    street_address_2 = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=False)
    post_code = models.CharField(max_length=15, blank=False, null=True)
    country = CountryField(blank_label='Country', blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=False, default=0
        )
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
        )

    def _order_no_generator(self):
        """
        Generate a unique order number at random
        Using UUID to do so.
        """
        return uuid.uuid4().hex.upper()

    def total_update(self):
        """
        every time a line item is added, update the the
        order total.
        """
        self.order_total = self.line_items.aggregate(
            Sum('line_item_total'))['line_item_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        If order number hasn't already been set,
        Override the original save and generate new order number.
        """
        if not self.order_number:
            self.order_number = self._order_no_generator()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE,
        related_name='line_items'
        )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
        )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_item_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False
        )

    def save(self, *args, **kwargs):
        """
        If order number hasn't already been set,
        Override the original save and generate new order number.
        """
        self.line_item_total = self.quantity * self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Item: {self.product.name} on order {self.order.order_number}'
