from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# URL ( endpoints ) goes here

router = DefaultRouter()
router.register("", views.CommentsViewsets)

urlpatterns = [
    path("comments/", include(router.urls)),
]
