from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class ContentView(APIView):
    def get(self, request):
        pass

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
