"""
Strip config, 
Webhook Handling
"""
from django.conf import settings
from django.http import HttpResponse
import json
import time

from profiles.models import CustomerProfile
from .models import Order, OrderLineItem
from products.models import Product
from django.http import HttpResponse


class StripeWH_Handler:
    """
    Stripe WebHook Handling.
    """
    def __init__(self, request):
        self.request  = request

    def handle_event(self, event):
        """
        Webhook event handler.
        """
        return HttpResponse(
            content=f'Unhandled Webhook Received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Webhook event handler for payment_intent.succeeded
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        order_total = round(intent.charges.data[0].amount / 100, 2)
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = CustomerProfile.objects.get(user__username=username)
            if save_info:
                profile.user.phone_number = shipping_details.phone,
                profile.user.house_name = shipping_details.address.house_name,
                profile.user.street_address_1 = shipping_details.address.line1,
                profile.user.street_address_2 = shipping_details.address.line2,
                profile.user.city = shipping_details.address.city,
                profile.user.post_code = shipping_details.address.post_code,
                profile.user.country = shipping_details.address.country,
                profile.save()
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    house_name__iexact=shipping_details.address.house_name,
                    street_address_1__iexact=shipping_details.address.line1,
                    street_address_2__iexact=shipping_details.address.line2,
                    city__iexact=shipping_details.address.city,
                    post_code__iexact=shipping_details.address.post_code,
                    country__iexact=shipping_details.address.country,
                    order_total=order_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook Received: {event["type"]} | SUCCESS, Verified order already in database',
                status=200
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    customer_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    post_code=shipping_details.address.post_code,
                    city=shipping_details.address.city,
                    street_address_1=shipping_details.address.line1,
                    street_address_2=shipping_details.address.line2,
                    house_name=shipping_details.address.house_name,
                    order_total=order_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook Received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Webhook event handler for payment_intent.payment_failed
        """
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )