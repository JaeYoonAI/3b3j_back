from rest_framework import serializers
from contents.models import Content, MovieContent, MusicContent, GameContent, Comment


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


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.nickname

    class Meta:
        model = Comment
        fields = (
            "id",
            "movie_content",
            "music_content",
            "game_content",
            "rate",
            "content",
            "user",
        )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "movie_content",
            "music_content",
            "game_content",
            "rate",
            "content",
        )
