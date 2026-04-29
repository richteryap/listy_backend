from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'id',
            'title',
            'content',
            'author',
            'is_list',
            'list_items',
            'is_trashed',
            'is_archived',
            'is_pinned',
            'image_url',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'author',
            'created_at',
            'updated_at'
        ]