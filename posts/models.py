from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    price = models.CharField(max_length=50, null=True)
    surplus = models.IntegerField(default = 50)
    view_count = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    seller = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
class Reviw(models.Model):
    content = models.TextField()
    score = models.IntegerField(default = 10)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
