from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show(request):
    return HttpResponse('Урок номер два.')

