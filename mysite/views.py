from django.shortcuts import render
from blog.models import Article


def index(request):
    objs = Article.objects.all()[:3]  # 全ての記事を取得
    context = {
        'title': 'Really Site',
        'articles': objs,
    }
    return render(request, 'mysite/index.html', context)

def login(request):
    context = {

    }
    if request.method == 'POST':
        context['req'] = request.POST
    return render(request, 'mysite/login.html', context)

