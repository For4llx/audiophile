from django.urls import path
from .views import ProductIndexView, ProductDetailView

urlpatterns = [
    path("products/", ProductIndexView.as_view(), name="products"),
    path("1/", ProductDetailView.as_view(), name="product"),
]
