from rest_framework import viewsets, status
from rest_framework.response import Response

from . import models
from . import serializers

# Create your views here.


# Like Viewsets
class LikeViewsets(viewsets.ModelViewSet):
    queryset = models.Likes.objects.all()
    serializer_class = serializers.LikeSerializer

    def get_queryset(self):
        return models.Likes.objects.filter(profile=self.request.user.Profile)  # type: ignore

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            profile=request.user.Profile, post=serializer.validated_data.get("post")
        )
        return Response("Liked", status=status.HTTP_201_CREATED)
