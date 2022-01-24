from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator


def index(request):
    objs = Article.objects.all()
    paginator = Paginator(objs, 2)  # 1ページに表示する記事数 2
    page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'blog/blogs.html', context)


def article(request, pk):
    obj = Article.objects.get(pk=pk)
    # print(obj) # 検証用
    context = {
        'article': obj
    }
    return render(request, 'blog/article.html', context)
