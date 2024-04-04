from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# URL ( endpoints ) goes here

router = DefaultRouter()
router.register("profile", views.ProfileViewsets)
router.register("followings", views.FollowingsViewsets, basename="profile-followings")
router.register("followers", views.FollowersViewsets, basename="profile-followers")

urlpatterns = [
    # user endpoints
    path("register/user/", views.UserRegisterView.as_view()),
    path("user/login/", views.UserLoginView.as_view()),
    path("user/logout/", views.UserLogoutView.as_view()),
    # profile endpoints
    path("profile/", include(router.urls)),
]
