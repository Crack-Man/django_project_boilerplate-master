# Generated by Django 2.2.10 on 2020-06-06 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_order_categoryuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='categoryUser',
        ),
    ]
