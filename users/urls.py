from django.urls import path, include
from users import views
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("signup_api/", views.UserView.as_view(), name="user_view"),
    path("mock/", views.mockView.as_view(), name="mock_view"),
    path(
        "api/token/",
        views.CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("<int:user_id>/", views.ProfileView.as_view(), name="profile_view"),
]
