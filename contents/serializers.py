from rest_framework import serializers
from contents.models import Content, MovieContent, MusicContent, GameContent, Comment


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


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieContent, MusicContent, GameContent
        fields = "__all__"


class MovieContentSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    comments_count = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()

    def get_comments_count(self, obj):
        return obj.comment_set.count()

    def get_avg_rating(self, obj):
        comments = Comment.objects.filter(movie_content=obj)
        if 0 < len(comments):
            total_rating = 0
            for comment in comments:
                total_rating += comment.rate
            avg_rating = total_rating / len(comments)
            return round(avg_rating, 1)
        else:
            return None

    class Meta:
        model = MovieContent
        fields = "__all__"


class MusicContentSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    comments_count = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()

    def get_comments_count(self, obj):
        return obj.comment_set.count()

    def get_avg_rating(self, obj):
        comments = Comment.objects.filter(music_content=obj)
        if 0 < len(comments):
            total_rating = 0
            for comment in comments:
                total_rating += comment.rate
            avg_rating = total_rating / len(comments)
            return round(avg_rating, 1)
        else:
            return None

    class Meta:
        model = MusicContent
        fields = "__all__"


class GameContentSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    comments_count = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()

    def get_comments_count(self, obj):
        return obj.comment_set.count()

    def get_avg_rating(self, obj):
        comments = Comment.objects.filter(game_content=obj)
        if 0 < len(comments):
            total_rating = 0
            for comment in comments:
                total_rating += comment.rate
            avg_rating = total_rating / len(comments)
            return round(avg_rating, 1)
        else:
            return None

    class Meta:
        model = GameContent
        fields = "__all__"
