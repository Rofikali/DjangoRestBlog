from enum import unique
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, models.CASCADE, related_name='post')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # img = models.ImageField(upload_to='Images', default='default.jpg')

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title
