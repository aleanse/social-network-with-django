from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.username



class Post(models.Model):
    title = models.CharField(max_length=30)
    text_post = models.TextField(max_length=200)
    image = models.ImageField( upload_to='user/covers/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='posts')
