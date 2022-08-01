from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


# Receiver decorator for post save signals from the OrderLineItem model.
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    When line item is updated/created update order total figure.
    """
    instance.order.total_update()


# Receiver decorator for post save signals from the OrderLineItem model.
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    When line item is deleted update order total figure.
    """
    instance.order.total_update()
