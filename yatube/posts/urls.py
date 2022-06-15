# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('group_list.html', views.group_posts),
    path('index.html', views.index),
    path('', views.index),
]
