# Generated by Django 2.2.10 on 2020-06-22 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20200621_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='recording',
            name='name',
            field=models.CharField(default=1, max_length=140, verbose_name='Как к Вам обращаться?'),
            preserve_default=False,
        ),
    ]