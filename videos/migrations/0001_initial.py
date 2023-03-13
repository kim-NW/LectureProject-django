# Generated by Django 4.1.7 on 2023-03-13 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("ledetailes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("videoFile", models.URLField()),
                ("videoLength", models.IntegerField(default=0)),
                (
                    "ledetail",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video",
                        to="ledetailes.ledetaile",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
