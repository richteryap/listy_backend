from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    # This translates React's camelCase into Django's snake_case
    isList = serializers.BooleanField(source='is_list', required=False)
    listItems = serializers.JSONField(source='list_items', required=False, allow_null=True)
    isTrashed = serializers.BooleanField(source='is_trashed', required=False)
    isArchived = serializers.BooleanField(source='is_archived', required=False)
    isPinned = serializers.BooleanField(source='is_pinned', required=False)
    imageUrl = serializers.URLField(source='image_url', required=False, allow_null=True, allow_blank=True)
    createdAt = serializers.DateTimeField(source='created_at', read_only=True)
    updatedAt = serializers.DateTimeField(source='updated_at', read_only=True)

    class Meta:
        model = Note
        # Notice we are using the camelCase names here so React understands them
        fields = [
            'id', 'title', 'content', 'author', 'isList', 'listItems', 
            'isTrashed', 'isArchived', 'isPinned', 'imageUrl', 
            'createdAt', 'updatedAt'
        ]
        read_only_fields = ['id', 'author', 'createdAt', 'updatedAt']