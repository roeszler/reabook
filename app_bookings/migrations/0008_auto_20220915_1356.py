# Generated by Django 3.2.15 on 2022-09-15 13:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookings', '0007_auto_20220915_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_data',
        ),
        migrations.AlterField(
            model_name='booking',
            name='duration',
            field=models.ForeignKey(blank=True, default='00:15', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_bookings.slot'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='slot',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_phone',
            field=models.IntegerField(blank=True, default='00X1 123 456 789', null=True),
        ),
    ]