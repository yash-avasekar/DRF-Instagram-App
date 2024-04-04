from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# Post URL ( endpoints )

router = DefaultRouter()
router.register("", views.PostsViewets)

urlpatterns = [
    path("posts/", include(router.urls)),
]
