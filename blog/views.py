from django.shortcuts import render
from django.http import HttpResponse


def article(request):
    context = {}
    return render(request, 'blog/article.html', context)

