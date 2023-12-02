from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
import stripe
from course.models import Course
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.encoding import smart_str
from django.http import JsonResponse
from user.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages


stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    price_in_cents = int(course.price * 100)

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "unit_amount": price_in_cents,
                "product_data": {
                    "name": course.title,
                },
            },
            "quantity": 1
        }],
        mode="payment",
        
        success_url=request.build_absolute_uri(reverse("payment:course-success")),
        cancel_url=request.build_absolute_uri(reverse("payment:course-cancel")),
        metadata= {
            'course_id': course.id,
            'user_id': request.user.id
        }
    )

    return redirect(session.url)


@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = smart_str(request.body)   # We're getting the payload which is what's sent us from Stripe and going to decode this into a string to be compatible with Python
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]  # Here we're retrieven the signature from the request. 
                                                        # Stripe signs the webhook payload with this signature and we'll use it for verification

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_ENDPOINT_SECRET # This method is used to construct an event using the data provided inside and then verify the authenticity
        )
    except ValueError:
        return JsonResponse({'error': 'Invalid payload'}, status=400) # THis will be raised if the payload is invalid.
    
    except stripe.error.SignatureVerificationError:
        return JsonResponse({'error': 'Invalid signature'}, status=400) # And this one is raised if the signature verification fails.
    
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"] # If everything is good this variable will contain our metadata (and other data) from "create_checkout_session" view
        handle_checkout_session(session) # And we call this other view to do the logic and unlock the course for the user

    return JsonResponse({'status':'success'})


def handle_checkout_session(session):
    course_id = session["metadata"]["course_id"]
    user_id = session["metadata"]["user_id"]
    user = CustomUser.objects.get(pk=user_id)
    course = get_object_or_404(Course, pk=course_id)
    course.subscribers.add(user)


@login_required
def course_success(request):
    messages.success(request, "Thanks for your pruchase!")
    return redirect(reverse('course:course-list'))


@login_required
def course_cancel(request):
    return redirect(reverse('course:course-list'))