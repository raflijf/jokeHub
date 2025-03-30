from django.db import models
from uuid import uuid4
from accounts.models import User
from django.utils.text import slugify
# Create your models here.
class Category(models.Model) : 
    name = models.CharField(max_length=15, unique=True)
    type = models.CharField(max_length=7,  default='jokes')
    slug = models.SlugField(max_length=20, blank=True)

    def save(self, *args, **kwargs) :
        self.slug = slugify(self.name)
        super().save(*args, **kwargs) 

class Post(models.Model) : 
    uuid = models.UUIDField(default=uuid4, unique=True, editable=False, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=270, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=7, default='jokes')

class Reaction(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='react')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='react')
    type = models.CharField(max_length=8, null=True)

    class Meta :
        unique_together = ('user', 'post')

class Comment(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    content = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    