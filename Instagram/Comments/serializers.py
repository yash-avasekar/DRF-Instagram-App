from rest_framework import serializers

from . import models

# Serializers goes here


# Comments Serializer
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = ["url", "id", "profile", "post", "comment", "created_at"]
        extra_kwargs = {
            "profile": {"read_only": True},
            "created_at": {"read_only": True},
        }
