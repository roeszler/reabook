# Generated by Django 3.2.15 on 2022-09-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookings', '0014_auto_20220915_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='id',
        ),
        migrations.AlterField(
            model_name='slot',
            name='duration',
            field=models.DurationField(max_length=68400, primary_key=15, serialize=False, verbose_name=0),
        ),
    ]
