from django.shortcuts import render
from django.views.generic import TemplateView


class ProductIndexView(TemplateView):
    """Display Products"""

    template_name = "products/index.html"


class ProductDetailView(TemplateView):
    """Display Product Detail"""

    template_name = "products/product.html"
