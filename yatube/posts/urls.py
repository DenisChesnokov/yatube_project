# posts/urls.py
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('group_list.html', views.group_posts, name='group_posts'),
    path('index.html', views.index, name='index'),
    path('', views.index),
]
