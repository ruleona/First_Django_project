from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show(request):
    return HttpResponse('Урок номер два.')

def items(request):
    return HttpResponse('Вы перешли в раздел items')