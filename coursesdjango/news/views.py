from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    # Получаем данные из формы:
    if request.method == 'POST':
        form = ArticleForm(request.POST) #Создается объект класса ArticleForm, содержащий все данные, которые ввел пользователь
        if form.is_valid(): # Метод класса ModelForm, проверяющий, корректно ли введены данные.
            form.save()
            return redirect('news_home')  # Выполняется переадресация на домашнюю страницу
        else:
            error = 'Форма была неверной'
    form = ArticleForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)