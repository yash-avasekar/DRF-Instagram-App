from rest_framework import serializers

from . import models

# Serializers goes here


# Like Serializer
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Likes
        fields = ["url", "id", "profile", "post"]
        extra_kwargs = {
            "profile": {"read_only": True},
        }
