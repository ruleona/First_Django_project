from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, ImageField

from .models import Article


# Этот файл связывает поля формы с объектом Articles. Создается новый класс:
class ArticleForm(ModelForm):
    class Meta:
        model = Article  # Класс связывается с моделью Article
        fields = ['title', 'anons', 'full_text', 'date', 'article_img']  # Указываются поля

        # Для того, чтобы у элементов формы появились атрибуты, создаем словарь:
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'article_img': ImageField()

        }

# class ImageForm(ModelForm):
#     class Meta:
#         model = Image
#         fields = ('title', 'image')
