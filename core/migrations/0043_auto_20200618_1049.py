# Generated by Django 2.2.10 on 2020-06-18 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0042_auto_20200618_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='new',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='1592441370', verbose_name='Ссылка на салон'),
        ),
        migrations.AlterField(
            model_name='new',
            name='slug',
            field=models.SlugField(default='1592441370', verbose_name='Ссылка на статью'),
        ),
    ]
