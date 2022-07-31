
import stripe

from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

@require_POST
@csrf_exempt
def webhook(request):
    """
    Stripe webhook listener.

    """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        """
        Payload = Invalid
        """
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        """
        Signature = Invalid.
        """
        return HttpResponse(status=400)
    except Exception as e:
        """
        Catch exceptions.
        """
        return HttpResponse(content=e, status=400)
    
    # WebHook Handler.
    handler  = StripeWH_Handler(request)
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }
    # fetch WH from STRIPE
    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)
    response = event_handler(event)
    return response