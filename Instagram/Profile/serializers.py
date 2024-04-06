from rest_framework import serializers

from . import models

# Serializer goes here


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer is used to serialize and deserialize User objects.

    Attributes:
        Meta (class): Nested class defining metadata options for the serializer.
            model (Model): The model class that the serializer is based on.
            fields (list): The fields to include in the serialized representation.
            extra_kwargs (dict): Additional keyword arguments for customizing field behavior.

    Example:
        To serialize a User object, initialize the serializer with the object:
        ```
        serializer = UserSerializer(user_instance)
        serialized_data = serializer.data
        ```
    """

    class Meta:
        model = models.User
        fields = ["id", "email", "username", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }


# User Login Serializer
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username", "password"]


# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.

    This serializer is used to serialize Profile objects, providing a representation of profile data.

    Attributes:
        url (str): A SerializerMethodField representing the URL for the profile.

    Methods:
        get_url(self, instance): Method to get the URL for the profile.
    """

    url = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()  # type:ignore
    following = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
        fields = [
            "id",
            "url",
            "profile_picture",
            "username",
            "name",
            "bio",
            "followers",
            "following",
        ]

    def get_url(self, instance):
        """
        Get the URL for the profile.

        This method returns the URL for the profile based on the request context.

        Args:
            instance (Profile): The Profile object.

        Returns:
            str: The URL for the profile.
        """
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(
                f"/api/profile/profile/{instance.username}/"
            )

    def get_followers(self, instance):
        return instance.follower.count()

    def get_following(self, instance):
        return instance.following.count()


# Following Serializer
class FollowingSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = models.Relation
        fields = "__all__"
        extra_kwargs = {
            "follower": {"read_only": True},
        }

    def get_url(self, instance):
        """
        Get the URL for the profile.

        This method returns the URL for the profile based on the request context.

        Args:
            instance (Profile): The Profile object.

        Returns:
            str: The URL for the profile.
        """
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(f"/api/profile/followings/{instance.id}/")


# Follower Serializer
class FollowerSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = models.Relation
        fields = "__all__"
        extra_kwargs = {
            "following": {"read_only": True},
        }

    def get_url(self, instance):
        """
        Get the URL for the profile.

        This method returns the URL for the profile based on the request context.

        Args:
            instance (Profile): The Profile object.

        Returns:
            str: The URL for the profile.
        """
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(f"/api/profile/followers/{instance.id}/")
