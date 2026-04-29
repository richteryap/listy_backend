from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

# A router automatically generates all the endpoints (GET, POST, PUT, DELETE) for our ViewSet
router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
]