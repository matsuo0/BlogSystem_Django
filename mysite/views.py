from django.shortcuts import render, redirect
from blog.models import Article
from django.contrib.auth.views import LoginView
from mysite.forms import UserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


def index(request):
    ranks = Article.objects.order_by('-count')[:2] # -をつけることで降順
    objs = Article.objects.all()[:3]  # 全ての記事を取得
    context = {
        'title': 'Really Site',
        'articles': objs,
        'ranks' : ranks,
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

            # ログインさせる
            login(request, user)
            messages.success(request, '登録完了')
            return redirect('/')
    return render(request, 'mysite/auth.html', context)


@login_required
def mypage(request):
    context = {}
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, '送信完了')
    return render(request, 'mysite/mypage.html', context)

def contact(request):
    context = {}
    return render(request, 'mysite/contact.html', context)
