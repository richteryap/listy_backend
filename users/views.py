from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import EmailTokenObtainSerializer
from .models import CustomUser
from .serializers import RegisterSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    # Override the default global restriction so guests can actually sign up
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class EmailTokenObtainView(TokenObtainPairView):
    serializer_class = EmailTokenObtainSerializer