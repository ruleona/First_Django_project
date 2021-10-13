from django.urls import path, re_path
from . import views

urlpatterns = [
    path('items/', views.items),
    path('about/', views.about, name='about'),
    re_path(r'^item/([0-9]{4})/$', views.year_archive, name='year_archive'),
    re_path(r'^item/([0-9]{4,5})/([0-9]{2}$)', views.year_month, name='year_month'),
    re_path(r'^item/(?P<year>[\d]{4})/(?P<month>[\d]{2})/(?P<day>[\d]{2})$', views.day_archive, name='day_archive'),
    re_path(r'^book$', views.book_title),
    re_path(r'^book/page/(?P<page_number>[\d]+)', views.book_page),
    re_path(r'^$', views.index, name='home'),
]