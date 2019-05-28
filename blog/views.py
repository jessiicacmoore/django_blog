from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

from datetime import date
from blog.models import Article, Comment


def root(request):
    return HttpResponseRedirect('home')

def home_page(request):
    context = {'articles': Article.objects.filter(draft=False).order_by('-published_date')}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def post_show(request, id):
  post = get_object_or_404(Article, id=id)
  article_comments = Comment.objects.filter(article=id)
  context = {'post': post, 'comments': article_comments}
  response = render(request, 'post.html', context)
  return HttpResponse(response)

@require_http_methods(['POST'])
def create_comment(request):
  user_article = request.POST['article']
  user_message = request.POST['message']
  user_name = request.POST['name']
  
  Comment.objects.create(name=user_name, message=user_message, article=Article.objects.get(id=user_article))
  return redirect('post_page', id=user_article) 
