
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class RegisterView(APIView):
    def get(self, request):
        return Response({'message': 'Register endpoint stub'})

class LoginView(APIView):
    def get(self, request):
        return Response({'message': 'Login endpoint stub'})

class ProfileView(APIView):
    def get(self, request):
        return Response({'message': 'Profile endpoint stub'})

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer