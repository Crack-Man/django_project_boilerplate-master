# Generated by Django 2.2.10 on 2020-06-18 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0045_auto_20200618_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='1592448467', verbose_name='Ссылка на салон'),
        ),
        migrations.AlterField(
            model_name='new',
            name='slug',
            field=models.SlugField(default='1592448467', verbose_name='Ссылка на статью'),
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('call', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('auth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]