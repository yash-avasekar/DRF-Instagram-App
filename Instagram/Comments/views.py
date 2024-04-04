from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from .permissions import IsCommentOwnerOrPostOwnerOrReadOnly

# Create your views here.


# Comments Viewsets
class CommentsViewsets(viewsets.ModelViewSet):
    permission_classes = [IsCommentOwnerOrPostOwnerOrReadOnly, IsAuthenticated]
    queryset = models.Comments.objects.all()
    serializer_class = serializers.CommentsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            profile=request.user.Profile,
            post=serializer.validated_data.get("post"),
            comment=serializer.validated_data.get("comment"),
        )
        return Response("Comment added.", status=status.HTTP_201_CREATED)
