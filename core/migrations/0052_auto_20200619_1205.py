# Generated by Django 2.2.10 on 2020-06-19 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_auto_20200619_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='1592532353', verbose_name='Ссылка на салон'),
        ),
        migrations.AlterField(
            model_name='new',
            name='slug',
            field=models.SlugField(default='1592532353', verbose_name='Ссылка на статью'),
        ),
    ]
