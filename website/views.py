from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from products.models import Customer, Order


class IndexView(TemplateView):
    """Display Home page"""

    template_name = "website/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer, created = Customer.objects.get_or_create(
            device=self.request.COOKIES.get("device")
        )
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        context["order"] = order

        return context

    def post(self, request):
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
