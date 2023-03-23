from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Customer, Order


class IndexView(TemplateView):
    """Display Home page"""

    template_name = "website/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer, created = Customer.objects.get_or_create(
            device=self.request.COOKIES["device"]
        )
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        context["order"] = order

        return context


class ProductView(TemplateView):
    """Display Products"""

    template_name = "website/product-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer, created = Customer.objects.get_or_create(
            device=self.request.COOKIES["device"]
        )
        context["order"] = Order.objects.get(customer=customer, complete=False)

        return context
