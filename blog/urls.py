from django.urls import path, include
from . import views

urlpatterns = [
    #path('/', views.test),
    path('article/', views.article)
]
