import factory
from factory import Faker

from posts.models import Post


class PostFactory(factory.django.DjangoModelFactory):
    username = Faker("user_name")
    title = Faker("name")
    content = Faker("name")

    class Meta:
        model = Post
