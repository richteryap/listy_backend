from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # CRITICAL: Locks down the API

    def get_queryset(self):
        # Security: Only return notes owned by the logged-in user
        return Note.objects.filter(author=self.request.user).order_by('-updated_at')

    def perform_create(self, serializer):
        # Security: Automatically set the author to the logged-in user
        serializer.save(author=self.request.user)

    # THIS FIXES YOUR REACT 404 ERROR!
    # It catches: DELETE /api/notes/cleanup-trash/
    @action(detail=False, methods=['delete'], url_path='cleanup-trash')
    def cleanup_trash(self, request):
        trashed_notes = self.get_queryset().filter(is_trashed=True)
        deleted_count, _ = trashed_notes.delete()
        return Response(
            {'message': f'Permanently deleted {deleted_count} trashed notes.'}, 
            status=status.HTTP_200_OK
        )