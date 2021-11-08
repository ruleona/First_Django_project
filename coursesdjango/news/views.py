from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, \
    DeleteView  # Класс, необходимый для динамически отображаемых страниц, на основе которого создадим свой новый класс

from .forms import ArticleForm  # Импортируем форму
from .models import Article


def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    # Получаем данные из формы:
    error = ''
    img_obj = object()
    if request.method == 'POST':
        form = ArticleForm(request.POST,
                           request.FILES)  # Создается объект класса ArticleForm, содержащий все данные, которые ввел пользователь
        if form.is_valid():  # Метод класса ModelForm, проверяющий, корректно ли введены данные.
            form.save()
            img_obj = form.instance
            return redirect('news_home')  # Выполняется переадресация на домашнюю страницу
        else:
            data = {
                'form': form,
                'error': 'Форма была неверной'
            }
            return render(request, 'news/create.html', data)
    else:
        form = ArticleForm()
        data = {'form': form}
        return render(request, 'news/create.html', data)


# def image_upload_view(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'index.html', {'form': form})


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article'  # название ключа, по которому будем передавать запись внутрь шаблона


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticleForm


class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/news-delete.html'
