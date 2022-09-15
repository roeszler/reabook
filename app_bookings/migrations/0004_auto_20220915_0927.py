# Generated by Django 3.2.15 on 2022-09-15 09:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_properties', '0016_property_selected'),
        ('app_bookings', '0003_auto_20220913_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('date', models.DateField()),
                ('duration', models.IntegerField(default=15)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_lunch', models.TimeField(default=13)),
                ('finish_lunch', models.TimeField(default=14)),
                ('start_day', models.TimeField(default=9)),
                ('finish_day', models.TimeField(default=17)),
                ('creation_date', models.DateTimeField()),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_properties.property')),
            ],
            options={
                'verbose_name_plural': 'Slots',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('f_name', models.CharField(max_length=254)),
                ('l_name', models.CharField(max_length=254)),
                ('username', models.CharField(blank=True, max_length=254, null=True, unique=True)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_phone', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(max_length=254)),
                ('is_active', models.BooleanField(default=False)),
                ('is_agent', models.BooleanField(default=False)),
                ('is_owner', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='AppointmentTypes',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='friendly_name',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='booking',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_properties.property'),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=254),
        ),
        migrations.AddField(
            model_name='slot',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_bookings.user'),
        ),
        migrations.AddField(
            model_name='booking',
            name='duration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_bookings.slot'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_bookings.user'),
        ),
    ]
