# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
import time
from django.contrib.auth.models import User
from django.utils.text import slugify

CATEGORY_CHOICES = (
    ('S', u'Обычный'),
    ('H', u'На дому')
)

CATEGORY_USER = (
    (u'К', u'Клиент'),
    (u'М', u'Мастер')
)



class Item(models.Model):
    auth = models.ForeignKey('auth.User', on_delete=models.CASCADE,
    null=True)
    title = models.CharField(u"Название салона*", max_length=100)
    price = models.CharField(u"Стоимость*", max_length=100)
    discount_price = models.CharField(
        u"Стоимость со скидкой", max_length=100, blank=True, null=True)
    category = models.CharField(
        u"Категория мастера*", choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField(u"Ссылка на салон")
    description = models.CharField(u"Адрес", max_length=100, blank=True, null=True)
    info = models.TextField(
        u"Описание салона", max_length=10000, blank=True)
    services = models.TextField(
        u"Список услуг", max_length=10000, blank=True)
    image = models.ImageField(u"Обложка салона*", default='')
    image1 = models.ImageField(
        u"Примеры дизайнов", null=True, blank=True)
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
    status = models.BooleanField(u"Подтверждён", default=False)

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
    title = models.CharField(u"Ссылка на салон", max_length=140)
    name = models.CharField(u"ФИО", max_length=140)
    auth = models.ForeignKey('auth.User', on_delete=models.CASCADE,
    null=True)
    call = models.CharField(u"Номер телефона", max_length=100)
    text = models.TextField(u"Расскажите о предпочтительном времени, добавьте дополнительную информацию", max_length=140, blank=True)


class Image(models.Model):
    auth = models.ForeignKey('auth.User', on_delete=models.CASCADE,
    null=True)
    image = models.ImageField(
        u"Изображение", upload_to='media/', default='')
    status = models.BooleanField(default=False)



class New(models.Model):
    auth = models.ForeignKey('auth.User',on_delete=models.CASCADE,
    null=True)
    title = models.CharField(u"Заголовок", max_length=100)
    info = models.TextField(
        u"Содержание", max_length=10000)
    image = models.ImageField(
        u"Обложка", upload_to='media/', default='', blank=True)
    slug = models.SlugField(u"Ссылка на статью")
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
