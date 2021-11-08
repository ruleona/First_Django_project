from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    article_img = models.ImageField(upload_to='./%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'  # Выполняется переадресация на отредактированную статью

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

# class Image(models.Model):
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='news/img/%Y/%m/%d/', blank=True)
#
#     def __str__(self):
#         return self.title
