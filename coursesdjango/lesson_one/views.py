from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Listen', 'to', 'your', 'heart.'],
        'obj': {'персона': 'человек',
              'марафон': 'гонка бегунов длиной около 26 миль',
              'противостоять': 'оставаться сильным, несмотря на давление',
              'бежать': 'двигаться со скоростью'}
    }
    return render(request, 'lesson_one/index.html', data)


def about(request):
    return render(request, 'lesson_one/about.html')
