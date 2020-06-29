from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Category(models.Model):
    title = models.CharField('Название категории', max_length=50, null=False)
    slug = models.SlugField('Ссылка на категорию', max_length=50)

    def get_absolute_url(self):
        return reverse("category_post_list", kwargs={'category': self.slug})

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField('Название города', max_length=100)
    slug = AutoSlugField(unique=True, populate_from='name')

    def __str__(self):
        return self.name


class Ad(models.Model):
    """Модель обьявления о продаже"""
    title = models.CharField('Заголовок', max_length=100, null=False)
    description = models.TextField('Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField('Фото', upload_to='images/', null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_DEFAULT, default="Россия")
    price = models.PositiveIntegerField("Цена",  null=False, default=0)
    publication_date = models.TimeField('Дата публикации', auto_now=True)
    moderated = models.BooleanField('Модерация', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ad_detail", kwargs={"pk": self.pk, 'category': self.category.slug, 'city': self.city.slug})

