from django.db import models

PAYMENT_METHODS = [
    ("emoney", "e-Money"),
    ("cash_on_delivery", "Cash on Delivery"),
]


class Billing(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)


class Shipping(models.Model):
    address = models.CharField(max_length=500)
    zip_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class Payment(models.Model):
    payment_method = models.CharField(
        choices=PAYMENT_METHODS, max_length=50, blank=False, default="emoney"
    )
    emoney_number = models.CharField(max_length=9, blank=True)
    emoney_pin = models.CharField(max_length=4, blank=True)
