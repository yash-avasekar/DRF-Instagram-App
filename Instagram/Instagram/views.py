from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


# Endpoints
class ApiEndpoints(generics.ListAPIView):
    """
    A view to list available API endpoints along with their URLs.

    Attributes:
        None

    Methods:
        list(self, request): Retrieves a dictionary containing API endpoints and their URLs.
            Args:
                request: The request sent by the client.
            Returns:
                Response: A JSON response containing a dictionary of API endpoints and their URLs.
    """

    permission_classes = [AllowAny]

    def list(self, request):
        endpoints = {
            "register_user": "http://localhost:8000/api/register/user/",
            "user_login": "http://localhost:8000/api/user/login/",
            "user_logout": "http://localhost:8000/api/user/logout/",
            "profile": "http://localhost:8000/api/profile/profile/",
            "profile_followings": "http://localhost:8000/api/profile/followings/",
            "profile_followers": "http://localhost:8000/api/profile/followers/",
            "posts": "http://localhost:8000/api/posts/",
            "likes": "http://localhost:8000/api/likes/",
            "comments": "http://localhost:8000/api/comments/",
        }
        return Response(endpoints, status=status.HTTP_200_OK)
