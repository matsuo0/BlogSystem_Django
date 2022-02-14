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

from django.contrib.sitemaps.views import sitemap
from config.sitemaps import StaticeViewSitemap, BlogSitemap

# ページ単位でキャッシュ
# from django.views.decorators.cache import cache_page

sitemaps = {
    "static": StaticeViewSitemap,
    "blog": BlogSitemap,
}

# example.com/
# 上か順に呼ばれることに気をつけること
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('mysite.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name="django.contrib.sitemaps.views.sitemap")
]
