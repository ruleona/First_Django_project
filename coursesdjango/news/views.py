from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm  # Импортируем форму
from django.views.generic import DetailView, UpdateView, DeleteView # Класс, необходимый для динамически отображаемых страниц, на основе которого создадим свой новый класс

def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article' #название ключа, по которому будем передавать запись внутрь шаблона


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'

    form_class = ArticleForm


class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/news-delete.html'


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