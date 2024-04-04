from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from . import models
from . import serializers
from . import utils
from .permissions import IsOwnerOrReadOnly

# Create your views here.


# User Register View
class UserRegisterView(generics.ListCreateAPIView):
    """
    A view for registering new users.

    Inherits from:
        generics.ListCreateAPIView

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for serializing User objects.
        search_fields (list of str): The fields to search against.

    Methods:
        create(self, request, *args, **kwargs):
            Handles the creation of a new user.
            Args:
                request (Request): The HTTP request object.
                *args: Additional positional arguments.
                **kwargs: Additional keyword arguments.
            Returns:
                Response: A response indicating the status of the user creation process.

    """

    permission_classes = [AllowAny]
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    search_fields = ["username", "name"]

    def create(self, request, *args, **kwargs):
        """
        Handles the creation of a new user.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A response indicating the status of the user creation process.
        """
        return utils.userProfileCreate(self, request)


class UserLoginView(generics.CreateAPIView):
    """
    A view for user authentication and login.

    Inherits from:
        generics.CreateAPIView

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for serializing User objects.

    Methods:
        create(self, request, *args, **kwargs):
            Handles the user login process.
            Args:
                request (Request): The HTTP request object.
                *args: Additional positional arguments.
                **kwargs: Additional keyword arguments.
            Returns:
                Response: A response indicating the status of the login process.

    """

    permission_classes = [AllowAny]
    queryset = models.User.objects.all()
    serializer_class = serializers.UserLoginSerializer

    def create(self, request, *args, **kwargs):
        """
        Handles the user login process.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A response indicating the status of the login process.
        """
        return utils.userLogin(request)


# User Logout View
class UserLogoutView(generics.CreateAPIView):
    """
    A view for user logout.

    Inherits from:
        generics.CreateAPIView

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for serializing User objects.

    Methods:
        create(self, request):
            Handles the user logout process.
            Args:
                request (Request): The HTTP request object.
            Returns:
                Response: A response indicating the status of the logout process.
    """

    queryset = models.User.objects.all()
    serializer_class = serializers.UserLoginSerializer

    def create(self, request):
        """
        Handles the user logout process.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A response indicating the status of the logout process.
        """
        return utils.userLogout(request)


# Profile Viewsets
class ProfileViewsets(viewsets.ModelViewSet):
    """
    A viewset for handling profile-related operations.

    Inherits from:
        viewsets.ModelViewSet

    Attributes:
        queryset (QuerySet): The queryset of Profile objects.
        serializer_class (Serializer): The serializer class for serializing Profile objects.
        lookup_field (str): The field used to look up Profile objects.
        search_fields (list of str): The fields to search against.

    Methods:
        create(self, request, *args, **kwargs):
            Returns a method not allowed response since creation is not allowed via this viewset.

        update(self, request, *args, **kwargs):
            Handles updating a profile instance.
            Args:
                request (Request): The HTTP request object.
                *args: Additional positional arguments.
                **kwargs: Additional keyword arguments.
            Returns:
                Response: A response indicating the status of the update process.

        perform_destroy(self, instance):
            Performs the deletion of a profile instance.
            Args:
                instance: The profile instance to be deleted.

    """

    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    lookup_field = "username"
    search_fields = ["username", "name"]

    def create(self, request, *args, **kwargs):
        """
        Returns a method not allowed response since creation is not allowed via this viewset.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A method not allowed response.
        """
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        """
        Handles updating a profile instance.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A response indicating the status of the update process.
        """
        return utils.updateProfile(self, request)

    def perform_destroy(self, instance):
        """
        Performs the deletion of a profile instance.

        Args:
            instance: The profile instance to be deleted.
        """
        return utils.deleteUserProfile(instance)


# Following View
class FollowingsViewsets(viewsets.ModelViewSet):
    """
    A viewset for managing user followings.

    Inherits from:
        viewsets.ModelViewSet

    Attributes:
        queryset (QuerySet): The queryset of Relation objects.
        serializer_class (Serializer): The serializer class for serializing Relation objects.

    Methods:
        get_queryset(self):
            Retrieves the queryset of followings associated with the current user.
            Returns:
                QuerySet: The filtered queryset.

        create(self, request, *args, **kwargs):
            Handles following a user.
            Args:
                request (Request): The HTTP request object.
                *args: Additional positional arguments.
                **kwargs: Additional keyword arguments.
            Returns:
                Response: A response indicating the status of the follow operation.

        update(self, request, *args, **kwargs):
            Returns a method not allowed response since updating is not allowed via this viewset.

        destroy(self, request, *args, **kwargs):
            Returns a method not allowed response since deleting is not allowed via this viewset.
    """

    queryset = models.Relation.objects.all()
    serializer_class = serializers.FollowingSerializer

    def get_queryset(self):
        """
        Retrieves the queryset of followings associated with the current user.

        Returns:
            QuerySet: The filtered queryset.
        """
        return models.Relation.objects.filter(follower=self.request.user.Profile)  # type: ignore

    def create(self, request, *args, **kwargs):
        """
        Handles following a user.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A response indicating the status of the follow operation.
        """
        return utils.follow(self, request)

    def update(self, request, *args, **kwargs):
        """
        Returns a method not allowed response since updating is not allowed via this viewset.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A method not allowed response.
        """
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        """
        Returns a method not allowed response since deleting is not allowed via this viewset.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A method not allowed response.
        """
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Follower View
class FollowersViewsets(viewsets.ModelViewSet):
    """
    A viewset for managing user followers.

    Inherits from:
        viewsets.ModelViewSet

    Attributes:
        queryset (QuerySet): The queryset of Relation objects.
        serializer_class (Serializer): The serializer class for serializing Follower objects.

    Methods:
        get_queryset(self):
            Retrieves the queryset of followers associated with the current user.
            Returns:
                QuerySet: The filtered queryset.

        create(self, request, *args, **kwargs):
            Returns a method not allowed response since creation is not allowed via this viewset.

        update(self, request, *args, **kwargs):
            Returns a method not allowed response since updating is not allowed via this viewset.
    """

    queryset = models.Relation.objects.all()
    serializer_class = serializers.FollowerSerializer

    def get_queryset(self):
        """
        Retrieves the queryset of followers associated with the current user.

        Returns:
            QuerySet: The filtered queryset.
        """
        return models.Relation.objects.filter(following=self.request.user.Profile)  # type: ignore

    def create(self, request, *args, **kwargs):
        """
        Returns a method not allowed response since creation is not allowed via this viewset.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A method not allowed response.
        """
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        """
        Returns a method not allowed response since updating is not allowed via this viewset.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A method not allowed response.
        """
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
