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
        context["product"] = Product.objects.get(slug=slug)
        return context
