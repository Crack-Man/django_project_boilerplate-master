# Generated by Django 2.2.10 on 2020-06-07 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20200607_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(default='1591501390', verbose_name='Ссылка на статью'),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='1591501390', verbose_name='Ссылка на салон'),
        ),
    ]
