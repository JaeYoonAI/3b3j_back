# Generated by Django 4.2.6 on 2023-10-11 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("contents", "0006_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="game_content",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contents.gamecontent",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="movie_content",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contents.moviecontent",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="music_content",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contents.musiccontent",
            ),
        ),
    ]
