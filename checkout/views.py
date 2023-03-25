from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .form import BillingForm, ShippingForm, PaymentForm
from products.models import Customer, Order


class CheckoutView(TemplateView):
    """Display Checkout"""

    template_name = "checkout/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(device=self.request.COOKIES.get("device"))
        context["order"] = Order.objects.get(customer=customer, complete=False)
        context["billing_form"] = BillingForm()
        context["shipping_form"] = ShippingForm()
        context["payment_form"] = PaymentForm()
        return context

    def post(self, request):
        if request.POST.get("remove") == "Remove all":
            customer, created = Customer.objects.get_or_create(
                device=self.request.COOKIES.get("device")
            )
            order = Order.objects.get(customer=customer, complete=False)
            order.delete()

            return redirect("/")
        return redirect("/checkout/success")


class SuccessView(TemplateView):

    template_name = "checkout/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(device=self.request.COOKIES.get("device"))
        context["order"] = Order.objects.get(customer=customer, complete=False)
        context["billing_form"] = BillingForm()
        context["shipping_form"] = ShippingForm()
        context["payment_form"] = PaymentForm()
        return context

    def post(self, request):
        if request.POST.get("remove") == "Remove all":
            customer, created = Customer.objects.get_or_create(
                device=self.request.COOKIES.get("device")
            )
            order = Order.objects.get(customer=customer, complete=False)
            order.delete()

            return redirect("/")
        customer, created = Customer.objects.get_or_create(
            device=self.request.COOKIES.get("device")
        )
        order = Order.objects.get(customer=customer, complete=False)
        order.delete()

        return redirect("/")
