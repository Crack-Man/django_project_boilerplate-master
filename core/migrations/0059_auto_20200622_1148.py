# Generated by Django 2.2.10 on 2020-06-22 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_recording_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='name',
            field=models.CharField(max_length=140, verbose_name='ФИО'),
        ),
    ]