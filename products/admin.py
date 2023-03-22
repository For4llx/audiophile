from django.contrib import admin
from .models import (
    ProductImage,
    CategoryImage,
    GalleryImage,
    Include,
    Gallery,
    Product,
    Order,
    OrderItem,
    Customer,
)

admin.site.register(
    [
        ProductImage,
        CategoryImage,
        GalleryImage,
        Include,
        Gallery,
        Product,
        Order,
        OrderItem,
        Customer,
    ]
)
