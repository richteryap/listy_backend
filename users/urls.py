from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, EmailTokenObtainView

urlpatterns = [
    # The login endpoint that returns the Access and Refresh tokens
    path('login/', EmailTokenObtainView.as_view(), name='token_obtain_pair'),
    
    # The endpoint React will hit silently in the background to keep the user logged in
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Our custom registration endpoint
    path('register/', RegisterView.as_view(), name='register'),
]