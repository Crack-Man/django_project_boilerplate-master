from django import forms
from .models import Image, Item, New
from django.forms import ModelForm

CAT_CHOICES = (
    ('S', 'Professional'),
    ('SW', 'Normal'),
    ('OW', 'At home')
)


class AddSaloon(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'title',
            'price',
            'discount_price',
            'category',
            'description',
            'info',
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
        fields = ('image', )


class News(forms.ModelForm):
    class Meta:
        model = New
        fields = ('title', 'info', 'image')


class Images(forms.ModelForm):
    Image = forms.ImageField(label="Добавьте картинку")
