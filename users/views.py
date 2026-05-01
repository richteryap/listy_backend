from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
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
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated] # Must have a valid JWT token

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'email': user.email,
        })