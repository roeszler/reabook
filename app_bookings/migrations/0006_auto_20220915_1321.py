# Generated by Django 3.2.15 on 2022-09-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookings', '0005_auto_20220915_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='friendly_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_name',
            field=models.CharField(blank=True, default='booking_data', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='slot_name',
            field=models.CharField(blank=True, default='slot_data', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_data',
            field=models.CharField(blank=True, default='user_data', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='day_finish',
            field=models.TimeField(default='17:00:00'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='day_start',
            field=models.TimeField(default='09:00:00'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='duration',
            field=models.TimeField(default='00:15'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='lunch_finish',
            field=models.TimeField(default='14:00:00'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='lunch_start',
            field=models.TimeField(default='13:00:00'),
        ),
    ]