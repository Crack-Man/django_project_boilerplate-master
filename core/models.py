from django.conf import settings
from django.db import models
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('S', 'Professional'),
    ('SW', 'Normal'),
    ('OW', 'At home')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    discount_price = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    info = models.TextField(
        max_length=140, default='Writte about your page', blank=True)
    image = models.ImageField(help_text="put your principal image", default='')
    image1 = models.ImageField(
        help_text="put your first  image", default='', blank=True)
    image2 = models.ImageField(
        help_text="put your second  image", default='', blank=True)
    image3 = models.ImageField(
        help_text="put your third  image", default='', blank=True)
    image4 = models.ImageField(
        help_text="put your last  image", default='', blank=True)
    image5 = models.ImageField(
        help_text="put your last  image", default='', blank=True)
    image6 = models.ImageField(
        help_text="put your last  image", default='', blank=True)
    image7 = models.ImageField(
        help_text="put your last  image", default='', blank=True)
    image8 = models.ImageField(
        help_text="put your last  image", default='', blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
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
