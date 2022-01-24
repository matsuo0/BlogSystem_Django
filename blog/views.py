from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article


def index(request):
    objs = Article.objects.all()
    context = {
        'articles': objs,
    }
    return render(request, 'blog/blogs.html', context)


def article(request, pk):
    obj = Article.objects.get(pk=pk)
    # print(obj) # 検証用
    context = {
        'article': obj
    }
    return render(request, 'blog/article.html', context)
