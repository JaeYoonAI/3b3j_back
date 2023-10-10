# Generated by Django 4.2.6 on 2023-10-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contents", "0002_moviecontent"),
    ]

    operations = [
        migrations.CreateModel(
            name="GameContent",
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
                ("rank", models.CharField(max_length=25)),
                ("title", models.CharField(max_length=50)),
                ("genre", models.CharField(max_length=25)),
                ("image", models.ImageField(blank=True, upload_to="%y/%m/")),
                ("release_machine", models.CharField(max_length=50)),
                ("release_date", models.CharField(max_length=25)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="MusicContent",
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
                ("rank", models.CharField(max_length=25)),
                ("title", models.CharField(max_length=50)),
                ("artist", models.CharField(max_length=50)),
                ("album_name", models.CharField(max_length=50)),
                ("cover", models.ImageField(blank=True, upload_to="%y/%m/")),
            ],
        ),
    ]
