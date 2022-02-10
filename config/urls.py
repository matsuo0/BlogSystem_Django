"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.urls import path
from django.contrib import admin
from django.urls import path, include
from mysite import views
# from blog import views as b_view
from django.contrib.auth.views import LogoutView

# ページ単位でキャッシュ
# from django.views.decorators.cache import cache_page


# example.com/
# 上か順に呼ばれることに気をつけること
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('blog/', include('blog.urls')),
    path('signup/', views.signup),
    # path('mypage/', views.mypage),
    path('mypage/', views.MypageView.as_view()),
    # path('contact/', views.contact),
    path('contact/', views.ContactView.as_view()),
    path('pay/', views.PayView.as_view()),
    #path('cache_test/', cache_page(30)(views.cache_test)),
]
