# Generated by Django 4.1.7 on 2023-03-13 07:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0005_rename_cartm_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="rating",
        ),
    ]
