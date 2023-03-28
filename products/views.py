from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import Product, Customer, Order, OrderItem


class ProductIndexView(TemplateView):
    """Display Products"""

    template_name = "products/index.html"

    def get_context_data(self, category, **kwargs):
        context = super().get_context_data(**kwargs)
        customer, created = Customer.objects.get_or_create(
            device=self.request.COOKIES.get("device")
        )
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        context["order"] = order
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

    def post(self, request, category, slug=None):
        if request.POST.get("checkout") == "Checkout":
            customer, created = Customer.objects.get_or_create(
                device=self.request.COOKIES.get("device")
            )
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False
            )
            quantities = request.POST.getlist("quantity")
            for index, item in enumerate(order.orderitem_set.all()):
                item.quantity = quantities[index]
                item.save()
            return redirect("/checkout")
        if request.POST.get("remove") == "Remove all":
            customer, created = Customer.objects.get_or_create(
                device=self.request.COOKIES.get("device")
            )
            order = Order.objects.get(customer=customer, complete=False)
            order.delete()

            return redirect("/")


class ProductDetailView(TemplateView):
    """Display Product Detail"""

    template_name = "products/product.html"

    def get_context_data(self, category, slug, **kwargs):
        context = super().get_context_data(**kwargs)
        customer, created = Customer.objects.get_or_create(
            device=self.request.COOKIES.get("device")
        )
        context["order"] = Order.objects.get(customer=customer, complete=False)
        context["product"] = Product.objects.get(slug=slug)
        return context

    def post(self, request, slug, category):
        if request.POST.get("add") == "Add to cart":
            product = Product.objects.get(slug=slug)
            customer, created = Customer.objects.get_or_create(
                device=self.request.COOKIES.get("device")
            )
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False
            )
            orderItem, created = OrderItem.objects.get_or_create(
                order=order, product=product
            )
            orderItem.quantity = request.POST["quantity"]
            orderItem.save()
            return redirect(f"/{category}/{slug}")
        if request.POST.get("checkout") == "Checkout":
            customer, created = Customer.objects.get_or_create(
                device=self.request.COOKIES.get("device")
            )
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False
            )
            quantities = request.POST.getlist("quantity")
            for index, item in enumerate(order.orderitem_set.all()):
                item.quantity = quantities[index]
                item.save()
            return redirect("/checkout")
        if request.POST.get("remove") == "Remove all":
            customer, created = Customer.objects.get_or_create(
                device=self.request.COOKIES.get("device")
            )
            order = Order.objects.get(customer=customer, complete=False)
            order.delete()

            return redirect("/")
