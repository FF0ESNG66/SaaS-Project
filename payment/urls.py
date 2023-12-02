from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path("<int:course_id>/", views.create_checkout_session, name="create-checkout-session"),
    path("course-success/", views.course_success, name="course-success"),
    path("course-cancel/", views.course_cancel, name="course-cancel"),
    path("stripe/webhook/", views.stripe_webhook, name="stripe-webhook")
]