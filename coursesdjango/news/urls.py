from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
]