from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Post
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,PostSerializer

    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    permission_classes=[IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.all() 
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
