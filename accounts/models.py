from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from PIL import Image
import os
# Create your models here.
class User(AbstractUser) : 
    email = models.EmailField(unique=True)
    bio = models.CharField(blank=True, max_length=500)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=300, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/',  default='https://res.cloudinary.com/dg0m3qgxt/image/upload/v1744208107/whkig5d0oafqfowlm2tw.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
