from django.urls import path
from contents import views


urlpatterns = [
    path("", views.ContentView.as_view(), name="content_view"),
    path("movie/", views.MovieContentView.as_view(), name="movie_content_view"),
    path("music/", views.MusicContentView.as_view(), name="movie_content_view"),
    path("game/", views.GameContentView.as_view(), name="movie_content_view"),
    path(
        "int:content_id>/",
        views.ContentDetailView.as_view(),
        name="content_detail_view",
    ),
    path("comment/", views.CommentView.as_view(), name="comment_view"),
    path(
        "comment/<int:comment_id>/",
        views.CommentDetailView.as_view(),
        name="comment_detail_view",
    ),
    path("like/", views.LikeView.as_view(), name="like_view"),
]
