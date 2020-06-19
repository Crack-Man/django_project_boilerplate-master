# Generated by Django 2.2.10 on 2020-06-19 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_auto_20200619_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recording',
            name='host',
        ),
        migrations.RemoveField(
            model_name='recording',
            name='saloon',
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='1592532771', verbose_name='Ссылка на салон'),
        ),
        migrations.AlterField(
            model_name='new',
            name='slug',
            field=models.SlugField(default='1592532771', verbose_name='Ссылка на статью'),
        ),
    ]
