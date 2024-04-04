from rest_framework import serializers

from . import models


# Serializers goes here


# Posts Serializer
class PostsSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = models.Posts
        fields = ["url", "id", "post_picture", "description", "profile"]
        extra_kwargs = {
            "profile": {"read_only": True},
        }
