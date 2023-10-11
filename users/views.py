from django.shortcuts import render
from rest_framework.views import APIView
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.

def signup(request):
    return render(request, 'signup.html')

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
        return Response("get요청")
