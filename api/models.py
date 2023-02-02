from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.TextField(max_length=200)
    description=models.TextField(max_length=400)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title