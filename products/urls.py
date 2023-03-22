from django.urls import path
from .views import ProductIndexView, ProductDetailView

urlpatterns = [
    path("<str:category>/", ProductIndexView.as_view(), name="products"),
    path("<str:category>/<slug:slug>/", ProductDetailView.as_view(), name="product"),
]
