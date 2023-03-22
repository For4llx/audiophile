from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import Product, Customer, Order, OrderItem


class ProductIndexView(TemplateView):
    """Display Products"""

    template_name = "products/index.html"

    def get_context_data(self, category, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get_or_create(device=self.request.COOKIES["device"])
        context["order"] = Order.objects.get(customer=customer, complete=False)
        if category == "earphones":
            context["products"] = Product.objects.filter(category="earphones")
            context["category"] = "earphones"
        if category == "headphones":
            context["products"] = Product.objects.filter(category="headphones")
            context["category"] = "headphones"
        if category == "speakers":
            context["products"] = Product.objects.filter(category="speakers")
            context["category"] = "speakers"
        return context


class ProductDetailView(TemplateView):
    """Display Product Detail"""

    template_name = "products/product.html"

    def get_context_data(self, category, slug, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(device=self.request.COOKIES["device"])
        context["order"] = Order.objects.get(customer=customer, complete=False)
        context["product"] = Product.objects.get(slug=slug)
        return context

    def post(self, request, slug, category):
        product = Product.objects.get(slug=slug)
        customer, created = Customer.objects.get_or_create(
            device=request.COOKIES["device"]
        )
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(
            order=order, product=product
        )
        orderItem.quantity = request.POST["quantity"]
        orderItem.save()

        return redirect(f"/{category}/{slug}")

    def delete(self, request, slug, category):
        customer, created = Customer.objects.get_or_create(
            device=request.COOKIES["device"]
        )
        order = Order.objects.get(customer=customer, complete=False)
        orderItem = OrderItem.objects.filter(order=order)
        orderItem.delete()

        return redirect(f"/{category}/{slug}")
