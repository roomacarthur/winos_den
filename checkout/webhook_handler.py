"""
Strip config, 
Webhook Handling
"""

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
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Webhook event handler for payment_intent.payment_failed
        """
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )