from django.shortcuts import render


# Create your views here.

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'lesson_one/index.html', data)


def about(request):
    data = {
        'title': 'Обо мне'
    }
    return render(request, 'lesson_one/about.html', data)


def contacts(request):
    data = {
        'title': 'Контакты'
    }
    return render(request, 'lesson_one/contacts.html', data)
