# Generated by Django 5.1.2 on 2024-10-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("name", models.CharField(max_length=200)),
                ("price", models.CharField(max_length=200)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
