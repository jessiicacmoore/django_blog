from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
