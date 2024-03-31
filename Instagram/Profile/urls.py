from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# URL ( endpoints ) goes here

router = DefaultRouter()
router.register("profile", views.ProfileViewsets)
router.register("following", views.FollowingViewsets)
router.register("follower", views.FollowerViewsets)

urlpatterns = [
    path("register/user/", views.UserRegisterView.as_view()),
    path("user/login/", views.UserLoginView.as_view()),
    path("user/logout/", views.UserLogoutView.as_view()),
    path("user/", include(router.urls)),
]
