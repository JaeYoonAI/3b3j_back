# Generated by Django 4.2.6 on 2023-10-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contents", "0003_gamecontent_musiccontent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gamecontent",
            name="release_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="moviecontent",
            name="relese_date",
            field=models.DateField(),
        ),
    ]
