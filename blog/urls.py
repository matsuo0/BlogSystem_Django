from django.urls import path, include
from . import views

urlpatterns = [
    #path('/', views.test),
    path('<slug:pk>/', views.article)
]
