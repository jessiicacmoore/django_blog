from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from datetime import date
from blog.models import Article

def root(request):
    return HttpResponseRedirect('home')

def home_page(request):
    context = {'articles': Article.objects.filter(draft=False).order_by('-published_date')}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def post_show(request, id):
  post = contact = get_object_or_404(Article, id=id)
  context = {'post': post}
  response = render(request, 'post.html', context)
  return HttpResponse(response)