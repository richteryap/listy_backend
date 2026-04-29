from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import RegisterSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    # Override the default global restriction so guests can actually sign up
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer