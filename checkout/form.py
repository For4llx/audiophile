from django import forms
from .models import Billing, Shipping, Payment

PAYMENT_METHODS = [
    ("emoney", "e-Money"),
    ("cash_on_delivery", "Cash on Delivery"),
]


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input input--field", "placeholder": "Alexei Ward"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "input input--field", "placeholder": "+1 202-555-0136"}
            ),
            "email": forms.TextInput(
                attrs={"class": "input input--field", "placeholder": "alexei@mail.com"}
            ),
        }


class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = "__all__"
        widgets = {
            "address": forms.TextInput(
                attrs={
                    "class": "input input--field",
                    "placeholder": "1137 Williams Avenue",
                }
            ),
            "zip_code": forms.TextInput(
                attrs={"class": "input input--field", "placeholder": "10001"}
            ),
            "city": forms.TextInput(
                attrs={"class": "input input--field", "placeholder": "New York"}
            ),
            "country": forms.TextInput(
                attrs={"class": "input input--field", "placeholder": "United States"}
            ),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        widgets = {
            "payment_method": forms.RadioSelect(
                attrs={"class": "input radio clicker"}, choices=PAYMENT_METHODS
            ),
            "emoney_number": forms.TextInput(
                attrs={"class": "input input--field", "placeholder": "238521993"}
            ),
            "emoney_pin": forms.TextInput(
                attrs={"class": "input input--field", "placeholder": "6891"}
            ),
        }
