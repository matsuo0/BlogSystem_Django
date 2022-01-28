from django.shortcuts import render, redirect
from blog.models import Article
from django.contrib.auth.views import LoginView
from mysite.forms import UserCreationForm
from django.contrib import messages


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

    def form_valid(self, form):
        messages.success(self.request, 'ログイン完了')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'エラーあり！')
        return super().form_invalid(form)


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # 今回はパスワード、メールアドレスをValidationだったり、パスワードハッシュ化目的
        if form.is_valid():
            user = form.save(commit=False)
            # user.is_active = False  # 初期状態はTrueだが、メールの検証が必要なるためFalseと定義する
            user.save()
            messages.success(request, '登録完了')
            return redirect('/')
    return render(request, 'mysite/auth.html', context)

def mypage(request):
    context = {}
    return render(request, 'mysite/mypage.html', context)
