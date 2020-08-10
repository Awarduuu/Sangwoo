from django.db import models

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