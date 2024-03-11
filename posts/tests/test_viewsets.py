import pytest
from rest_framework import status

from django.urls import reverse

from posts.models import Post


@pytest.mark.django_db
class TestPostAPI:
    def test_posts_list(self, api_client, post):
        response = api_client.get(
            reverse("posts:posts-list")
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data.get("count") == 1
        assert post.id in [post.get("id") for post in response.data.get("results")]

    def test_posts_detail(self, api_client, post):
        response = api_client.get(
            reverse("posts:posts-detail", args=(post.id,))
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data.get("id") == post.id

    def test_create_post(self, api_client):
        data = {
            "username": "lorence",
            "title": "Test Post",
            "content": "Test Content for Test Post",
        }
        response = api_client.post(
            reverse("posts:posts-list"), data
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert Post.objects.count() == 1

    def test_put_post(self, api_client, post):
        data = {
            "username": "lorence",
            "title": "Test Post",
            "content": "Test Content for Test Post",
        }
        response = api_client.put(
            reverse("posts:posts-detail", args=(post.id,)), data
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data.get("username") == data.get("username")
        assert response.data.get("title") == data.get("title")
        assert response.data.get("content") == data.get("content")

    def test_patch_post(self, api_client, post):
        data = {
            "title": "Updated Post",
        }
        response = api_client.patch(
            reverse("posts:posts-detail", args=(post.id,)), data
        )

        assert response.status_code == status.HTTP_200_OK

        post.refresh_from_db()

        assert post.title == data.get("title")

    def test_delete_post(self, api_client, post):
        response = api_client.delete(
            reverse(
                "posts:posts-detail", args=(post.id,)
            ),
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Post.objects.count() == 0
