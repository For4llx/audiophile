from django.contrib import admin
from .models import (
    ProductImage,
    CategoryImage,
    GalleryImage,
    Include,
    Gallery,
    Product,
)

admin.site.register(
    [ProductImage, CategoryImage, GalleryImage, Include, Gallery, Product]
)
