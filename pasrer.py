import requests
from bs4 import BeautifulSoup


# 1번 파일이 실행될 때 환경변수에 현재 자신의 프로젝트의 settings.py파일 경로를 등록.
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alpha_critic.settings")

# 2번 실행파일에 Django 환경을 불러오는 작업.
import django

django.setup()


# 3번 크롤링을 하고 DB model에 저장.
from contents.models import MovieContent


def parse_movie():
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
        MovieContent(
            rank=rank, title=title, relese_date=relese_date, description=description
        )
        doc = {
            "rank": rank,
            "title": title,
            "relese_date": relese_date,
            "description": description,
        }
        return doc


def add_new_items(crawled_items):
    last_inserted_items = MovieContent.objects.last()
    if last_inserted_items is None:
        last_inserted_specific_id = ""
    else:
        last_inserted_specific_id = getattr(last_inserted_items, "title")

    doc = []
    for item in crawled_items:
        if item["title"] == last_inserted_specific_id:
            break
        doc.append(item)
    doc.reverse()

    for item in doc:
        print("new item added!! : " + item["title"])

        MovieContent(
            rank=item["rank"],
            title=item["title"],
            relese_data=item["relese_date"],
            description=item["description"],
        ).save()

    return doc


# movie_doc_list = parse_movie()

# for rank, title, relese_date, description in movie_doc_list.items():
#     MovieContent(
#         rank=rank, title=title, relese_date=relese_date, description=description
#     ).save()
