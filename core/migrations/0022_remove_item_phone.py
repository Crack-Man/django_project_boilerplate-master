# Generated by Django 2.2.10 on 2020-05-19 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20200519_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='phone',
        ),
    ]
