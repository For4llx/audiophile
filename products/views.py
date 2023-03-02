from django.shortcuts import render
from django.views.generic import TemplateView


class ProductIndexView(TemplateView):
    """Display Products"""

    template_name = "products/index.html"
