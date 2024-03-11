from rest_framework.routers import DefaultRouter

from django.urls import include, path

from posts.viewsets import PostViewSet


router = DefaultRouter()
router.register("", PostViewSet, basename="posts")

urlpatterns = [
    path("", include(router.urls)),
]
