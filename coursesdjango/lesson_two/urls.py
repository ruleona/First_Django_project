from django.urls import path, re_path
from . import views

urlpatterns = [
    path('lesson_two/', views.show),
]