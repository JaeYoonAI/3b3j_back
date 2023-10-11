from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from contents.models import Content, MovieContent, MusicContent, GameContent
from contents.serializers import (
    ContentSerializer,
    MovieContentSerializer,
    MusicContentSerializer,
    GameContentSerializer,
)
import requests
from bs4 import BeautifulSoup


class MovieContentView(APIView):
    def get(self, request):
        movie_contents = MovieContent.objects.all()
        serializer = MovieContentSerializer(movie_contents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MusicContentView(APIView):
    def get(self, request):
        music_contents = MusicContent.objects.all()
        serializer = MusicContentSerializer(music_contents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GameContentView(APIView):
    def get(self, request):
        game_contents = GameContent.objects.all()
        serializer = GameContentSerializer(game_contents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContentView(APIView):
    def get(self, request):
        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass


class ContentDetailView(APIView):
    def get(self, request, content_id):
        pass

    def post(self, request):
        pass


class CommentView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass


class CommentDetailView(APIView):
    def put(self, request):
        pass

    def delete(self, request):
        pass


class LikeView(APIView):
    def post(self, request):
        pass
