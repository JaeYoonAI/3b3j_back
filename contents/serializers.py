from rest_framework import serializers
from contents.models import Content, MovieContent, MusicContent, GameContent


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class MovieContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieContent
        fields = "__all__"


class MusicContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicContent
        fields = "__all__"


class GameContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameContent
        fields = "__all__"
