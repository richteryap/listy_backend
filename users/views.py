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
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class EmailTokenObtainView(TokenObtainPairView):
    serializer_class = EmailTokenObtainSerializer
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'birthday': getattr(user, 'birthday', None), 
        })

    def put(self, request):
        user = request.user
        data = request.data

        if 'username' in data:
            user.username = data['username']
        
        if 'birthday' in data:
            user.birthday = data['birthday']
            
        user.save()
        
        return Response({
            'message': 'Profile updated successfully',
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'birthday': getattr(user, 'birthday', None),
        })

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        new_password = request.data.get('new_password')

        if not new_password or len(new_password) < 6:
            return Response(
                {'error': 'Password must be at least 6 characters long.'}, 
                status=400
            )

        user.set_password(new_password)
        user.save()

        return Response({'message': 'Password updated successfully!'})