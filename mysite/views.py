import os

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from blog.models import Article
from mysite.forms import UserCreationForm, ProfileForm

from django.contrib.auth.decorators import login_required
from django.contrib.sitemaps import ping_google


@login_required
def ping(request):
    try:
        if request.user.is_admin:
            ping_google()
    except:
        pass
    return redirect('/')


def landing(request):
    context = {}
    return render(request, 'mysite/landing.html', context)


def index(request):
    ranks = Article.objects.order_by('-count')[:2]  # -をつけることで降順
    objs = Article.objects.all()[:3]  # 全ての記事を取得
    context = {
        'title': 'Really Site',
        'articles': objs,
        'ranks': ranks,
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


from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class MypageView(LoginRequiredMixin, View):

    def get(self, request):
        context = {}
        return render(request, 'mysite/mypage.html', context)

    def post(self, request):
        context = {}
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, '送信完了')


# @login_required
# def mypage(request):
#     context = {}
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         # print('is_validの手前です')
#         if form.is_valid():
#             # print('is_validの中です')
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             messages.success(request, '送信完了')
#     return render(request, 'mysite/mypage.html', context)


class ContactView(View):
    context = {
        'grecaptcha_sitekey': os.environ['GRECAPTCHA_SITEKEY'],
    }

    def get(self, request):
        return render(request, 'mysite/contact.html', self.context)

    def post(self, request):
        if request.method == "POST":
            recaptcha_token = request.POST.get("g-recaptcha-response")
            res = grecaptcha_request(recaptcha_token)
            if not res:
                messages.error(request, 'reCAPTCHAに失敗したようです。')
                render(request, 'mysite/contact.html', self.context)
            # --- email to me ---
            subject = 'お問合せがありました。'
            message = """お問合せがありました。 \n名前: {}\n メールアドレス: {}\n内容: {}""".format(
                request.POST.get('name'),
                request.POST.get('email'),
                request.POST.get('content'))
            email_from = os.environ['DEFAULT_EMAIL_FROM']
            email_to = [os.environ['DEFAULT_EMAIL_FROM']]
            send_mail(subject, message, email_from, email_to)
            # --- email ---
        return render(request, 'mysite/contact.html', self.context)


# def contact(request):
#     context = {
#         'grecaptcha_sitekey': os.environ['GRECAPTCHA_SITEKEY'],
#     }
#     if request.method == "POST":
#         recaptcha_token = request.POST.get("g-recaptcha-response")
#         res = grecaptcha_request(recaptcha_token)
#         if not res:
#             messages.error(request, 'reCAPTCHAに失敗したようです。')
#             render(request, 'mysite/contact.html', context)
#         # --- email to me ---
#         subject = 'お問合せがありました。'
#         message = """お問合せがありました。 \n名前: {}\n メールアドレス: {}\n内容: {}""".format(
#             request.POST.get('name'),
#             request.POST.get('email'),
#             request.POST.get('content'))
#         email_from = os.environ['DEFAULT_EMAIL_FROM']
#         email_to = [os.environ['DEFAULT_EMAIL_FROM']]
#         send_mail(subject, message, email_from, email_to)
#         # --- email ---
#     return render(request, 'mysite/contact.html', context)


def grecaptcha_request(token):
    from urllib import request, parse
    import json, ssl

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

    url = "https://www.google.com/recaptcha/api/siteverify"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {
        'secret': os.environ['GRECAPTCHA_SECRETKEY'],
        'response': token,
    }
    data = parse.urlencode(data).encode()
    req = request.Request(
        url,
        method="POST",
        headers=headers,
        data=data,
    )
    f = request.urlopen(req, context=context)
    response = json.loads(f.read())
    f.close()
    # print('---- response ----')
    # print(response)
    # print('---- response ----')
    # ---- response - ---
    # {'success': True, 'challenge_ts': '2022-02-04T04:03:23Z', 'hostname': 'testkey.google.com'}
    # ---- response - ---

    return response['success']


# FlaskをベースにDjangoにも同様の処理を入れていく
# https://pay.jp/docs/flask-checkout
import payjp


class PayView(View):
    payjp.api_key = os.environ['PAYJP_SECRET_KEY']
    public_key = os.environ['PAYJP_PUBLIC_KEY']
    amount = 1000

    def get(self, request):
        context = {
            'amount': self.amount,
            'public_key': self.public_key,
        }
        return render(request, 'mysite/pay.html', context)

    def post(self, request):
        customer = payjp.Customer.create(
            email='example@pay.jp',
            card=request.POST.get('payjp-token'),
        )
        charge = payjp.Charge.create(
            amount=self.amount,
            currency='jpy',
            customer=customer.id,
            description='支払いテスト'
        )
        context = {
            'amount': self.amount,
            'public_key': self.public_key,
            'charge': charge
        }
        return render(request, 'mysite/pay.html', context)
