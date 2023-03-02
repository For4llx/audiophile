from django.urls import path
from .views import ProductIndexView

urlpatterns = [
    path("products/", ProductIndexView.as_view(), name="products"),
]
