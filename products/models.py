from django.db import models


CATEGORIES = [
    ("earphones", "Earphones"),
    ("headphones", "Headphones"),
    ("speakers", "Speakers"),
]

IMAGE_TYPES = [
    ("preview", "Preview"),
    ("gallery-1", "Gallery 1"),
    ("gallery-2", "Gallery 2"),
    ("gallery-3", "Gallery 3"),
    ("product", "Product"),
]


class Image(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(choices=IMAGE_TYPES, max_length=50)
    mobile = models.CharField(max_length=1000)
    tablet = models.CharField(max_length=1000)
    desktop = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name} {self.type.capitalize()}"


class ProductImage(Image):
    pass


class CategoryImage(Image):
    pass


class GalleryImage(Image):
    pass


class Include(models.Model):
    quantity = models.IntegerField()
    item = models.CharField(max_length=1000)

    def __str__(self):
        return self.item


class Gallery(models.Model):
    first = models.ForeignKey(
        "GalleryImage", related_name="first", on_delete=models.CASCADE
    )
    second = models.ForeignKey(
        "GalleryImage", related_name="second", on_delete=models.CASCADE
    )
    third = models.ForeignKey(
        "GalleryImage", related_name="third", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.first.name

    class Meta:
        verbose_name_plural = "Galleries"


class Product(models.Model):
    slug = models.SlugField(max_length=1000)
    name = models.CharField(max_length=1000)
    image = models.ForeignKey("Image", on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORIES, max_length=1000)
    categoryImage = models.ForeignKey(
        "CategoryImage", related_name="categoryImage", on_delete=models.CASCADE
    )
    new = models.BooleanField()
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    features = models.TextField(max_length=1000)
    include = models.ManyToManyField("Include")
    gallery = models.ForeignKey("Gallery", on_delete=models.CASCADE)
    others = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.name
