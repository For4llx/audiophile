from django.shortcuts import render
from django.views.generic import TemplateView


class CheckoutView(TemplateView):
    """Display Checkout"""

    template_name = "checkout/index.html"
