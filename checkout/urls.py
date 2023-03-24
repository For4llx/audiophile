from django.urls import path
from .views import CheckoutView, SuccessView

urlpatterns = [
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("checkout/success", SuccessView.as_view(), name="success"),
]
