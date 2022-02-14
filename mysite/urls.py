# from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LogoutView
from mysite import views

app_name = "mysite"

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view()),
    path('signup/', views.signup),
    path('mypage/', views.MypageView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('pay/', views.PayView.as_view()),
    path('landing/', views.landing),

    # path('cache_test/', cache_page(30)(views.cache_test)),

    path('ping/', views.ping)
]