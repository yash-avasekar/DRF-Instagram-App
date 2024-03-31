from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# URL ( endpoints ) goes here

router = DefaultRouter()
router.register("", views.ProfileViewsets)

urlpatterns = [
    path("register/user/", views.UserRegisterView.as_view()),
    path("profile/", include(router.urls)),
]
