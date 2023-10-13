from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404
from contents.models import Content, MovieContent, MusicContent, GameContent, Comment
from contents.serializers import (
    ContentSerializer,
    MovieContentSerializer,
    MusicContentSerializer,
    GameContentSerializer,
    CommentSerializer,
    CommentCreateSerializer,
)
import requests
from bs4 import BeautifulSoup


def moviedetails(request, moviecontent_id):
    movie_detail = get_object_or_404(MovieContent, pk=moviecontent_id)
    return render(request, "moviedetails.html", {"moviecontent": movie_detail})


def musicdetails(request, musiccontent_id):
    music_detail = get_object_or_404(MusicContent, pk=musiccontent_id)
    return render(request, "musicdetails.html", {"musiccontent": music_detail})


def gamedetails(request, gamecontent_id):
    game_detail = get_object_or_404(GameContent, pk=gamecontent_id)
    return render(request, "gamedetails.html", {"gamecontent": game_detail})


def all_list(request):
    return render(request, "all_list.html")


class MovieContentView(APIView):
    def get(self, request):
        movie_contents = MovieContent.objects.all()
        serializer = MovieContentSerializer(movie_contents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieContentDetailView(APIView):
    def get(self, request, moviecontent_id):
        moviecontent = get_object_or_404(MovieContent, id=moviecontent_id)
        serializer = MovieContentSerializer(moviecontent)
        return Response(serializer.data)


class MusicContentView(APIView):
    def get(self, request):
        music_contents = MusicContent.objects.all()
        serializer = MusicContentSerializer(music_contents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MusicContentDetailView(APIView):
    def get(self, request, musiccontent_id):
        musiccontent = get_object_or_404(MusicContent, id=musiccontent_id)
        serializer = MusicContentSerializer(musiccontent)
        return Response(serializer.data)


class GameContentView(APIView):
    def get(self, request):
        game_contents = GameContent.objects.all()
        serializer = GameContentSerializer(game_contents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GameContentDetailView(APIView):
    def get(self, request, gamecontent_id):
        gamecontent = get_object_or_404(GameContent, id=gamecontent_id)
        serializer = GameContentSerializer(gamecontent)
        return Response(serializer.data)


class ContentView(APIView):
    def get(self, request):
        movie_contents = MovieContent.objects.all()
        music_contents = MusicContent.objects.all()
        game_contents = GameContent.objects.all()
        serializer = ContentSerializer(
            movie_contents, music_contents, game_contents, many=True
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class ContentDetailView(APIView):
    def get(self, request, content_id):
        pass


class CommentView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):
    def put(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            serializer = CommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)
