from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Display Home page"""

    template_name = "website/index.html"