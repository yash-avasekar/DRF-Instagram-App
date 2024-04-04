from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# URL ( endpoints ) goes here

router = DefaultRouter()
router.register("", views.LikeViewsets)

urlpatterns = [
    path("likes/", include(router.urls)),
]
