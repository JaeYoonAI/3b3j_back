from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from contents.models import Content
from contents.serializers import ContentSerializer
import requests
from bs4 import BeautifulSoup


class MovieView(APIView):
    def get(self, request):
        URL = "https://movie.daum.net/ranking/reservation"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        data = requests.get(URL, headers=headers)
        soup = BeautifulSoup(data.text, "html.parser")
        movie_list = soup.select("#mainContent > div > div.box_ranking > ol > li")

        for li in movie_list:
            rank = li.select_one(".rank_num").text
            title = li.select_one(".link_txt").text
            relese_date = li.select_one(".txt_info").text[-9:-1]
            description = li.select_one(".link_story").text.strip("\n ")
            doc = {
                "rank": rank,
                "title": title,
                "relese_date": relese_date,
                "description": description,
            }
            print(doc)

        return Response(doc, status=status.HTTP_200_OK)


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
