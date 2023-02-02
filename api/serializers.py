from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post
    
class UserSerializer(serializers.HyperlinkedModelSerializer
):
    class Meta:
        model=User
        fields=['url','username','email','password']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Post
        fields=['url','owner','title','description']