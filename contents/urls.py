from django.urls import path
from contents import views


urlpatterns = [
    path("", views.ContentView.as_view(), name="content_view"),
    path("movie/", views.MovieContentView.as_view(), name="movie_content_view"),
    path(
        "api/movie/<int:moviecontent_id>/",
        views.MovieContentDetailView.as_view(),
        name="movie_content_detail_view",
    ),
    path("movie/<int:moviecontent_id>/", views.moviedetails, name="moviedetails"),
    path("music/", views.MusicContentView.as_view(), name="movie_content_view"),
    path(
        "api/music/<int:musiccontent_id>/",
        views.MusicContentDetailView.as_view(),
        name="music_content_detail_view",
    ),
    path("music/<int:musiccontent_id>/", views.musicdetails, name="musicdetails"),
    path("game/", views.GameContentView.as_view(), name="movie_content_view"),
    path(
        "api/game/<int:gamecontent_id>/",
        views.GameContentDetailView.as_view(),
        name="game_content_detail_view",
    ),
    path("game/<int:gamecontent_id>/", views.gamedetails, name="gamedetails"),
    path("comments/", views.CommentView.as_view(), name="comment_view"),
    path(
        "comments/<int:comment_id>/",
        views.CommentDetailView.as_view(),
        name="comment_detail_view",
    ),
    path("all_list/", views.all_list),
]
