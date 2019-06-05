from django import forms
from .models import Article, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body", "draft", "author"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["message", "name"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
