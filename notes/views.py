from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer

    # 1. Security: Ensure users only see their OWN notes, not everyone's.
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user).order_by('-updated_at')

    # 2. Security: Automatically set the author to the logged-in user when creating a note.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)