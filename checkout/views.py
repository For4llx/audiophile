from django.shortcuts import render
from django.views.generic import TemplateView
from .form import BillingForm, ShippingForm, PaymentForm
from products.models import Customer, Order


class CheckoutView(TemplateView):
    """Display Checkout"""

    template_name = "checkout/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(device=self.request.COOKIES["device"])
        context["order"] = Order.objects.get(customer=customer, complete=False)
        context["billing_form"] = BillingForm()
        context["shipping_form"] = ShippingForm()
        context["payment_form"] = PaymentForm()
        return context
