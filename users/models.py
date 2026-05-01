from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    avatar_url = models.URLField(max_length=1024, null=True, blank=True)