from django.db import models
from django.db.models.functions import Now



class Post(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
