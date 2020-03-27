from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def article(request):
    articles = Article.objects.all().order_by("date")
    return render(request, "art/article.html", {"articles": articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, "art/article_detail.html", {"article": article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    return render(request, "art/article_create.html")
