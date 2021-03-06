# Generated by Django 2.2.10 on 2020-05-17 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0011_item_image4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AvailabilityOccurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('number', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='image3',
            field=models.ImageField(default='', help_text='put your third  image', upload_to=''),
        ),
        migrations.CreateModel(
            name='RoomReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(db_index=True)),
                ('end_time', models.DateTimeField(db_index=True)),
                ('approved', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservations', to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='core.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
