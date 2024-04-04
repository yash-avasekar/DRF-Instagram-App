from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout

from . import models

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# User Viewset


def userProfileCreate(self, request):
    """
    Creates a user profile.

    Args:
        self: The instance of the view.
        request (Request): The HTTP request object.

    Returns:
        Response: A response indicating the status of the user profile creation process.
    """
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = models.User.objects.create_user(
        email=serializer.validated_data.get("email"),
        username=serializer.validated_data.get("username"),
        password=serializer.validated_data.get("password"),
    )

    models.Profile.objects.create(
        user=user,
        username=user.username,
    ).save()

    user.save()
    return Response("User Account Created Successfully", status=status.HTTP_201_CREATED)


def userLogin(request):
    """
    Authenticates and logs in a user.

    Args:
        request (Request): The HTTP request object.

    Returns:
        Response: A response indicating the status of the login process.
    """
    user = authenticate(
        request,
        username=request.data.get("username").lower().replace(" ", ""),
        password=request.data.get("password"),
    )

    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"Token": f"Token {token.key}"}, status=status.HTTP_200_OK)
    return Response(
        "Invalid Username or Password.", status=status.HTTP_401_UNAUTHORIZED
    )


def userLogout(request):
    """
    Logs out a user.

    Args:
        request (Request): The HTTP request object.

    Returns:
        Response: A response indicating the status of the logout process.
    """
    Token.objects.filter(user=request.user).delete()
    logout(request)
    return Response("You are logged out.", status=status.HTTP_200_OK)


# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# Profile Viewset


def updateProfile(self, request):
    """
    Updates a profile instance.

    Args:
        self: The instance of the view.
        request (Request): The HTTP request object.

    Returns:
        Response: A response indicating the status of the update process.
    """
    serializer = self.serializer_class(
        self.get_object(), data=request.data, partial=True
    )
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data.get("user")
    user.username = serializer.validated_data.get("username")
    user.first_name = serializer.validated_data.get("name")
    user.save()
    serializer.save()
    return Response("Profile has been updated.", status=status.HTTP_200_OK)


def deleteUserProfile(instance):
    """
    Delete user profile and associated user.

    This function deletes the profile instance along with its associated user from the database.

    Args:
        instance: The profile instance to be deleted.

    Returns:
        None
    """
    user = instance.user
    user.delete()
    instance.delete()


# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# Following Viewset


def follow(self, request):
    """
    Follows or unfollows a user based on the request data.

    Args:
        self: The instance of the view.
        request (Request): The HTTP request object.

    Returns:
        Response: A response indicating the status of the follow operation.
    """
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    follow_profile = request.data.get("following")

    is_following = self.get_queryset().filter(
        follower=request.user.Profile, following=follow_profile
    )

    if is_following.exists() is not True:
        serializer.save(follower=request.user.Profile)
        return Response(
            f"Following {follow_profile}",
            status=status.HTTP_201_CREATED,
        )
    is_following.delete()
    return Response(f"Unfollowed {follow_profile}", status=status.HTTP_201_CREATED)
