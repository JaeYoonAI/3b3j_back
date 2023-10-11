from django.db import models

from users.models import User

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to="%y/%m/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


class MovieContent(models.Model):
    rank = models.CharField(max_length=25)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to="%y/%m/")
    relese_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return str(self.title)


class GameContent(models.Model):
    rank = models.CharField(max_length=25)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    image = models.ImageField(blank=True, upload_to="%y/%m/")
    release_machine = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return str(self.title)


class MusicContent(models.Model):
    rank = models.CharField(max_length=25)
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album_name = models.CharField(max_length=50)
    cover = models.ImageField(blank=True, upload_to="%y/%m/")

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_content = models.ForeignKey(
        MovieContent, null=True, blank=True, on_delete=models.CASCADE
    )
    music_content = models.ForeignKey(
        MusicContent, null=True, blank=True, on_delete=models.CASCADE
    )
    game_content = models.ForeignKey(
        GameContent, null=True, blank=True, on_delete=models.CASCADE
    )
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)
