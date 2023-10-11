from django.contrib import admin
from contents.models import Content, MovieContent, GameContent, MusicContent, Comment

# Register your models here.

admin.site.register(Content)
admin.site.register(MovieContent)
admin.site.register(GameContent)
admin.site.register(MusicContent)
admin.site.register(Comment)
