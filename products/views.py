from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product


class ProductIndexView(TemplateView):
    """Display Products"""

    template_name = "products/index.html"

    def get_context_data(self, category, **kwargs):
        context = super().get_context_data(**kwargs)
        if category == "earphones":
            context["products"] = Product.objects.filter(category="earphones")
        if category == "headphones":
            context["products"] = Product.objects.filter(category="headphones")
        if category == "speakers":
            context["products"] = Product.objects.filter(category="speakers")
        return context


class ProductDetailView(TemplateView):
    """Display Product Detail"""

    template_name = "products/product.html"
