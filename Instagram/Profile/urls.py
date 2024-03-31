from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# URL ( endpoints ) goes here

router = DefaultRouter()

urlpatterns = [
    path("profile/", include(router.urls), name="profile"),
]
