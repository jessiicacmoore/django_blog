from django import forms
from .models import Article



class PostForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ["title", "body", "draft", "author"]


class LoginForm(forms.Form):
	username = forms.CharField(max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())