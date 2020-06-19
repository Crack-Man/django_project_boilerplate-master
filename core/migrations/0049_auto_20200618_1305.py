# Generated by Django 2.2.10 on 2020-06-18 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_auto_20200618_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='1592449543', verbose_name='Ссылка на салон'),
        ),
        migrations.AlterField(
            model_name='new',
            name='slug',
            field=models.SlugField(default='1592449543', verbose_name='Ссылка на статью'),
        ),
        migrations.AlterField(
            model_name='recording',
            name='slug',
            field=models.CharField(max_length=140, verbose_name='Салон'),
        ),
    ]
