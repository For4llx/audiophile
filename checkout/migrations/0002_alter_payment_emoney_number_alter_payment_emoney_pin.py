# Generated by Django 4.1.7 on 2023-03-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="emoney_number",
            field=models.CharField(blank=True, max_length=9),
        ),
        migrations.AlterField(
            model_name="payment",
            name="emoney_pin",
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
