from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls.conf import re_path

from .models import *

# Create your views here.
menu = [
        {'title': "Discover", 'url_name': 'discover'},
        {'title': "Join", 'url_name': 'join'}
]


def index(request):
    # posts = Women.objects.all()
    context = {
        'menu': menu,
        # 'title': 'Main'
    }
    return render(request, 'women/index.html', context=context)


def discover(request):
    return render(request, 'women/discover.html', {'menu': menu, 'title': 'Discover'})


def join(request):
    return render(request, 'women/join.html', {'menu': menu, 'title': 'Join'})





def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
