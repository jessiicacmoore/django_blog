from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(validators=[MinLengthValidator(10)])
    draft = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")


class Comment(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
