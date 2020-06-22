# -*- coding: utf-8 -*-
from django import forms
from .models import Image, Item, New, Recording
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

CAT_CHOICES = (
    ('S', u'Обычный'),
    ('H', u'На дому')
)

CATEGORY_USER = (
    (u'К', u'Клиент'),
    (u'М', u'Мастер')
)


class AddSaloon(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'auth',
            'title',
            'slug',
            'price',
            'discount_price',
            'category',
            'description',
            'info',
            'services',
            'image',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'image6',
            'image7',
            'image8',
        )
        exclude = ['auth', 'slug']
    # Title = forms.CharField(label="Название салона")
    # Price = forms.FloatField(label="Стоимость")
    # Discount_Price = forms.FloatField(
    #     label="Стоимость со скидкой (необязательно)", required=False)
    # Сategory = forms.ChoiceField(
    #     label="Категория мастера", choices=CAT_CHOICES)
    # Description = forms.CharField(
    #     label="Адрес", max_length=140, required=False)
    # Info = forms.CharField(label="Описание салона",
    #                        max_length=140, required=False, widget=forms.Textarea)
    # Image = forms.ImageField(label="Обложка салона")
    # Image1 = forms.ImageField(label="Примеры дизайнов", required=False)
    # Image2 = forms.ImageField(label="", required=False)
    # Image3 = forms.ImageField(label="", required=False)
    # Image4 = forms.ImageField(label="", required=False)
    # Image5 = forms.ImageField(label="", required=False)
    # Image6 = forms.ImageField(label="", required=False)
    # Image7 = forms.ImageField(label="", required=False)
    # Image8 = forms.ImageField(label="", required=False)


class IMG(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'auth')
        exclude = ['auth']


class NewsForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ('title', 'slug', 'info', 'image', 'auth')
        exclude = ['slug', 'auth']

class Recordings(forms.ModelForm):
    class Meta:
        model = Recording
        fields = ('title', 'name', 'auth', 'call', 'text')
        exclude = ['title', 'auth']


class Images(forms.ModelForm):
    Image = forms.ImageField(label=u"Добавьте картинку")


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(label=u'Имя', max_length=100)
    last_name = forms.CharField(label=u'Фамилия', max_length=100)
    category = forms.ChoiceField(label=u'Категория', choices=CATEGORY_USER)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        category = self.cleaned_data['category']
        if category == u'М':
            user.is_staff = True
        user.save()
        if category == u'К':
            user.groups.add(Group.objects.get(name=u'Клиент'))
        elif category == u'М':
            user.groups.add(Group.objects.get(name=u'Мастер'))
            