import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient


from posts.tests.factories import PostFactory


register(PostFactory)


@pytest.fixture
def api_client():
    yield APIClient()
