from django.shortcuts import render
from blog.models import Article


def index(request):
    objs = Article.objects.all()  # 全ての記事を取得
    context = {
        'title': 'Really Site',
        'articles': objs,
    }
    return render(request, 'mysite/index.html', context)
