from django.conf import settings
from django.db import models
from django.shortcuts import reverse
import time
from django.contrib.auth.models import User
from django.utils.text import slugify

CATEGORY_CHOICES = (
    ('S', 'Обычный'),
    ('H', 'На дому')
)

CATEGORY_USER = (
    ('К', 'Клиент'),
    ('М', 'Мастер')
)



class Item(models.Model):
    auth = models.ForeignKey('auth.User', on_delete=models.CASCADE,
    null=True)
    title = models.CharField("Название салона", max_length=100)
    price = models.CharField("Стоимость", max_length=100)
    discount_price = models.CharField(
        "Стоимость со скидкой (необязательно)", max_length=100, blank=True, null=True)
    category = models.CharField(
        "Категория мастера", choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField("Ссылка на салон")
    description = models.TextField("Адрес", blank=True, null=True)
    info = models.TextField(
        "Описание салона", max_length=10000, blank=True)
    image = models.ImageField("Обложка салона", default='')
    image1 = models.ImageField(
        "Примеры дизайнов", null=True, blank=True)
    image2 = models.ImageField(
        "", null=True, blank=True)
    image3 = models.ImageField(
        "", null=True, blank=True)
    image4 = models.ImageField(
        "", null=True, blank=True)
    image5 = models.ImageField(
        "", null=True, blank=True)
    image6 = models.ImageField(
        "", null=True, blank=True)
    image7 = models.ImageField(
        "", null=True, blank=True)
    image8 = models.ImageField(
        "", null=True, blank=True)
    status = models.BooleanField("Подтверждён", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Brand, self).save(*args, **kwargs)


class Recording(models.Model):
    title = models.CharField("Ссылка на салон", max_length=140)
    auth = models.ForeignKey('auth.User', on_delete=models.CASCADE,
    null=True)
    call = models.CharField("Номер телефона", max_length=100)
    text = models.TextField("Расскажите о предпочтительном времени, добавьте дополнительную информацию", max_length=140, blank=True)


class Image(models.Model):
    auth = models.ForeignKey('auth.User', on_delete=models.CASCADE,
    null=True)
    image = models.ImageField(
        "Изображение", upload_to='media/', default='')
    status = models.BooleanField(default=False)



class New(models.Model):
    auth = models.ForeignKey('auth.User',on_delete=models.CASCADE,
    null=True)
    title = models.CharField("Заголовок", max_length=100)
    info = models.TextField(
        "Содержание", max_length=10000)
    image = models.ImageField(
        "Обложка", upload_to='media/', default='', blank=True)
    slug = models.SlugField("Ссылка на статью")
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("core:posts", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
