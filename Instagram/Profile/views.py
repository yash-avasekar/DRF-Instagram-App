from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from . import models
from . import serializers

# Create your views here.


class UserRegisterView(generics.ListCreateAPIView):
    """
    API View for user registration.

    This view allows users to register by providing their email, username, and password.

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for User objects.
        search_fields (list): The fields used for searching users.

    Methods:
        create(self, request, *args, **kwargs): Handles user registration by creating a new User and Profile object.
    """

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    search_fields = ["username", "name"]

    def create(self, request, *args, **kwargs):
        """
        Create a new user account.

        This method validates the input data and creates a new user account along with a corresponding profile.
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = models.User.objects.create_user(
            email=serializer.validated_data.get("email"),  # type: ignore
            username=serializer.validated_data.get("username"),  # type: ignore
            password=serializer.validated_data.get("password"),  # type: ignore
        )

        models.Profile.objects.create(
            user=user,
            username=user.username,
        ).save()

        user.save()
        return Response(
            "User Account Created Successfully", status=status.HTTP_201_CREATED
        )


class ProfileViewsets(viewsets.ModelViewSet):
    """
    API Viewset for managing user profiles.

    This viewset provides CRUD operations for managing user profiles.

    Attributes:
        queryset (QuerySet): The queryset of Profile objects.
        serializer_class (Serializer): The serializer class for Profile objects.
        lookup_field (str): The field used for looking up profiles.
        search_fields (list): The fields used for searching profiles.

    Methods:
        create(self, request, *args, **kwargs): Method not allowed.
        update(self, request, *args, **kwargs): Updates the profile details.
        perform_destroy(self, instance): Deletes the profile and its associated user.
    """

    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    lookup_field = "username"
    search_fields = ["username", "name"]

    def create(self, request, *args, **kwargs):
        """
        Method not allowed.

        This method returns an HTTP 405 Method Not Allowed response as profile creation is not supported.
        """
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        """
        Update user profile.

        This method updates the profile details including the username and name.
        """
        serializer = self.serializer_class(
            self.get_object(), data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get("user")  # type: ignore
        user.username = serializer.validated_data.get("username")  # type: ignore
        user.first_name = serializer.validated_data.get("name")  # type: ignore
        user.save()  # type: ignore
        serializer.save()
        return Response("Profile has been updated.", status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        """
        Delete user profile.

        This method deletes the profile along with its associated user.
        """
        user = instance.user
        user.delete()
        instance.delete()


# Following View
class FollowingViewsets(viewsets.ModelViewSet):
    queryset = models.Following.objects.all()
    serializer_class = serializers.FollowingSerializer

    def update(self, request, *args, **kwargs):
        return Response(
            "Method Not Allowed.", status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


# Follower View
class FollowerViewsets(viewsets.ModelViewSet):
    queryset = models.Follower.objects.all()
    serializer_class = serializers.FollowerSerializer

    def update(self, request, *args, **kwargs):
        return Response(
            "Method Not Allowed.", status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
