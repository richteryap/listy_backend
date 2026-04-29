from django.db import models
from django.conf import settings

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    author  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')
    
    is_list = models.BooleanField(default=False)
    list_items = models.JSONField(blank=True, null=True, default=list)
    
    is_trashed = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.title if self.title else 'Untitled Note'