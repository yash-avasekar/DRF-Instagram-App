from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout

from . import models
from . import serializers
from . import utils

# Create your views here.


# User Register View
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
        return utils.userProfileCreate(self, request, models, Response, status)


# User Login View
class UserLoginView(generics.CreateAPIView):
    """
    API View for user login.

    This view allows users to authenticate and obtain an authentication token for subsequent requests.

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for user login.

    Methods:
        create(self, request, *args, **kwargs): Handles user login by calling the utility function userLogin.
    """

    queryset = models.User.objects.all()
    serializer_class = serializers.UserLoginSerializer

    def create(self, request, *args, **kwargs):
        """
        Perform user login.

        This method authenticates the user based on the provided credentials and generates an authentication token.

        Returns:
            Response: The authentication token or an error message.
        """
        return utils.userLogin(request, authenticate, login, Token, Response, status)


# User Logout View
class UserLogoutView(generics.CreateAPIView):
    """
    API View for user logout.

    This view allows users to log out and invalidate their authentication token.

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for user login.

    Methods:
        create(self, request): Handles user logout by calling the utility function userLogout.
    """

    queryset = models.User.objects.all()
    serializer_class = serializers.UserLoginSerializer

    def create(self, request):
        """
        Perform user logout.

        This method invalidates the user's authentication token and logs them out.

        Returns:
            Response: A message confirming successful logout.
        """
        return utils.userLogout(request, Token, logout, Response, status)


# Profile Viewsets
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
        return utils.updateProfile(self, request, Response, status)

    def perform_destroy(self, instance):
        return utils.deleteUserProfile(self, instance)


# Following View
class FollowingViewsets(viewsets.ModelViewSet):
    queryset = models.Following.objects.all()
    serializer_class = serializers.FollowingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save(profile =)
        print("*" * 50)
        # print(self.get_object())
        print("*" * 50)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        return Response(
            "Method Not Allowed.", status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


# Follower View
class FollowerViewsets(viewsets.ModelViewSet):
    queryset = models.Follower.objects.all()
    serializer_class = serializers.FollowerSerializer

    def create(self, request, *args, **kwargs):
        return Response("follower")

    def update(self, request, *args, **kwargs):
        return Response(
            "Method Not Allowed.", status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
