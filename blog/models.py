from django.db import models
from django.core.validators import MinLengthValidator

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(validators=[MinLengthValidator(10)])
    draft = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)


class Comment(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
