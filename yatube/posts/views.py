# from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


# Главная страница
def index(request):
    return HttpResponse('Главная страница проекта Yatube')


# Страница с постами отфильтованными по группам
def group_posts(request, slug):
    return HttpResponse(f'Страница с постами группы: {slug}')
