# Generated by Django 4.1.7 on 2023-03-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Information",
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
                ("sDate", models.DateTimeField(auto_now_add=True)),
                ("situation", models.CharField(max_length=150)),
            ],
        ),
    ]
