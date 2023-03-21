# Generated by Django 4.1.7 on 2023-03-19 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Galleries",
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("preview", "Preview"),
                            ("gallery-1", "Gallery 1"),
                            ("gallery-2", "Gallery 2"),
                            ("gallery-3", "Gallery 3"),
                            ("product", "Product"),
                        ],
                        max_length=50,
                    ),
                ),
                ("mobile", models.CharField(max_length=1000)),
                ("tablet", models.CharField(max_length=1000)),
                ("desktop", models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Include",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("item", models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="CategoryImage",
            fields=[
                (
                    "image_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="products.image",
                    ),
                ),
            ],
            bases=("products.image",),
        ),
        migrations.CreateModel(
            name="GalleryImage",
            fields=[
                (
                    "image_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="products.image",
                    ),
                ),
            ],
            bases=("products.image",),
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(max_length=1000)),
                ("name", models.CharField(max_length=1000)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("earphones", "Earphones"),
                            ("headphones", "Headphones"),
                            ("speakers", "Speakers"),
                        ],
                        max_length=1000,
                    ),
                ),
                ("new", models.BooleanField()),
                ("price", models.IntegerField()),
                ("description", models.TextField(max_length=1000)),
                ("features", models.TextField(max_length=1000)),
                (
                    "gallery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.gallery",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="products.image"
                    ),
                ),
                ("include", models.ManyToManyField(to="products.include")),
                ("others", models.ManyToManyField(blank=True, to="products.product")),
                (
                    "categoryImage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categoryImage",
                        to="products.categoryimage",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="gallery",
            name="first",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="first",
                to="products.galleryimage",
            ),
        ),
        migrations.AddField(
            model_name="gallery",
            name="second",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="second",
                to="products.galleryimage",
            ),
        ),
        migrations.AddField(
            model_name="gallery",
            name="third",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="third",
                to="products.galleryimage",
            ),
        ),
    ]