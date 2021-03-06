# Generated by Django 2.2.10 on 2020-05-19 02:44

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20200519_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'warning')], max_length=1),
        ),
    ]
