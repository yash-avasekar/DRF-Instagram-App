# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# User Viewset


def userProfileCreate(self, request, models, Response, status):
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
    return Response("User Account Created Successfully", status=status.HTTP_201_CREATED)


def userLogin(request, authenticate, login, Token, Response, status):
    """
    Utility function for user login.

    This function authenticates the user based on the provided credentials and generates an authentication token.

    Args:
        request (Request): The HTTP request object.
        authenticate (function): Function to authenticate user credentials.
        login (function): Function to log in the user.
        Token (Model): Token model for generating authentication tokens.
        Response (class): Response class for returning HTTP responses.
        status (module): Module for HTTP status codes.

    Returns:
        Response: The authentication token or an error message.
    """
    user = authenticate(
        request,
        username=request.data.get("username").lower().replace(" ", ""),
        password=request.data.get("password"),
    )

    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"Token", f"Token {token.key}"}, status=status.HTTP_200_OK)
    return Response(
        "Invalid Username or Password.", status=status.HTTP_401_UNAUTHORIZED
    )


def userLogout(request, Token, logout, Response, status):
    """
    Utility function for user logout.

    This function invalidates the user's authentication token and logs them out.

    Args:
        request (Request): The HTTP request object.
        Token (Model): Token model for managing authentication tokens.
        logout (function): Function to log out the user.
        Response (class): Response class for returning HTTP responses.
        status (module): Module for HTTP status codes.

    Returns:
        Response: A message confirming successful logout.
    """
    Token.objects.filter(user=request.user).delete()
    logout(request)
    return Response("You are logged out.", status=status.HTTP_200_OK)


# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# Profile Viewset


def updateProfile(self, request, Response, status):
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


def deleteUserProfile(self, instance):
    """
    Delete user profile.

    This method deletes the profile along with its associated user.
    """
    user = instance.user
    user.delete()
    instance.delete()
