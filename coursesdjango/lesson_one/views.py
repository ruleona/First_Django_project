from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show(request):
    return HttpResponse('Содержимое урока № 1')

def home(request):
    return HttpResponse('Домашняя страница.')

def items(request):
    return HttpResponse('Вы находитесь в разделе items/')

def year_archive(request,  num):
    return HttpResponse(f'Добро пожаловать на страницу localhost/{num}')