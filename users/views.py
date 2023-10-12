from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from users.models import User
from users.serializers import (
    CustomTokenObtainPairSerializer,
    UserProfileSerializer,
    UserSerializer,
)
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.


def signup(request):
    return render(request, "signup.html")


def login(request):
    return render(request, "login.html")


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST
            )


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        user = request.user
        user.is_admin = True
        user.save()
        return Response("get요청")


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
