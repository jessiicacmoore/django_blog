from django.forms import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from datetime import date
from blog.models import Article, Comment
from blog.forms import PostForm, LoginForm, CommentForm


def root(request):
    return HttpResponseRedirect("home")


def home_page(request):
    context = {
        "articles": Article.objects.filter(draft=False).order_by("-published_date")
    }
    response = render(request, "index.html", context)
    return HttpResponse(response)


def post_show(request, id):
    post = get_object_or_404(Article, id=id)
    article_comments = Comment.objects.filter(article=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save()
    else:
        form = CommentForm()

    context = {"post": post, "comments": article_comments, "form": form}

    return render(request, "post.html", context)


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("post_page", id=post.id)
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, "post_new.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            pw = form.cleaned_data["password"]
            user = authenticate(username=username, password=pw)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            form.add_error("username", "Login failed")
    else:
        form = LoginForm()

    context = {"form": form}
    http_response = render(request, "login.html", context)
    return HttpResponse(http_response)


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def post_edit(request, id):
    article = get_object_or_404(Article, pk=id, user=request.user.pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("post_page", id=post.id)
    else:
        form = PostForm(instance=article)
    context = {"form": form}
    return render(request, "post_new.html", context)
