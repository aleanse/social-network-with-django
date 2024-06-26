from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.





class User(AbstractUser):
    def __str__(self):
        return self.username

    photo = models.ImageField(upload_to='images/photo_profile/', default='images/default.png')
    posts_likes = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True, related_name='author_likes')

    def contar_seguidores(self):
        return Seguidor.objects.filter(seguindo=self).count()
    

class Seguidor(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seguidor')
    seguindo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seguindo')
    data_seguindo = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('usuario', 'seguindo')

class Post(models.Model):
    title = models.CharField(max_length=30)
    text_post = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/posts/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    def total_likes(self):
        return self.likes.count()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)    
    class Meta:
        unique_together = ('user', 'post')









