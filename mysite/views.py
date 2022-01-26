from django.shortcuts import render
from blog.models import Article
from django.contrib.auth.views import LoginView
from mysite.forms import UserCreationForm


def index(request):
    objs = Article.objects.all()[:3]  # 全ての記事を取得
    context = {
        'title': 'Really Site',
        'articles': objs,
    }
    return render(request, 'mysite/index.html', context)


# def login(request):
#     context = {
#
#     }
#     if request.method == 'POST':
#         context['req'] = request.POST
#     return render(request, 'mysite/auth.html', context)

class Login(LoginView):
    template_name = 'mysite/auth.html'


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # 今回はパスワード、メールアドレスをValidationだったり、パスワードハッシュ化目的
        if form.is_valid():
            user = form.save(commit=False)
            #user.is_active = False  # 初期状態はTrueだが、メールの検証が必要なるためFalseと定義する
            user.save()
    return render(request, 'mysite/auth.html', context)
