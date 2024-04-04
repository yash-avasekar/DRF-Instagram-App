from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from . import models
from . import serializers
from .permissions import IsOwnerOrReadOnly


# Create your views here.


# Posts Viewsets
class PostsViewets(viewsets.ModelViewSet):

    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostsSeriliazer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=request.user.Profile)
        return Response("Post Created.", status=status.HTTP_201_CREATED)
