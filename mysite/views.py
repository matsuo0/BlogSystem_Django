from django.shortcuts import render


def index(request):
    context = {
        'title': 'Really Site'
    }
    return render(request, 'mysite/index.html', context)
