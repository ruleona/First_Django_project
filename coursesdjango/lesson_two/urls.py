from django.urls import path
from . import views

urlpatterns = [
    path(r'lesson_two/', views.show),
    path(r'items$', views.items)
]