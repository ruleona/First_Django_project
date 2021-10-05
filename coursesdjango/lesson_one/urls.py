from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'lesson_one/', views.show),
    path(r'items/', views.items, name='items'),
    re_path(r'^item/([0-9]{4})/$', views.year_archive, name='year_archive'),
    path(r'^$', views.home),

]