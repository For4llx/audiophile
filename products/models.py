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


class Order(models.Model):
    customer = models.ForeignKey(
        "Customer", on_delete=models.SET_NULL, null=True, blank=True
    )
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey("Order", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class Customer(models.Model):
    device = models.CharField(max_length=1000, null=True, blank=True)
