# posts/urls.py
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('/group/<slug>/', views.group_posts, name='group_list'),
    path('index.html', views.index, name='index'),
    path('', views.index),
    #path('group_list.html', views.group_posts, name='group_list'),   
]
