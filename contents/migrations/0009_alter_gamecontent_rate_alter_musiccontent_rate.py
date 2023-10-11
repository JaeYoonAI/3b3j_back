# Generated by Django 4.2.6 on 2023-10-11 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contents", "0008_gamecontent_rate_moviecontent_rate_musiccontent_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gamecontent",
            name="rate",
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="musiccontent",
            name="rate",
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
    ]
