# Generated by Django 3.2.15 on 2022-09-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookings', '0009_auto_20220915_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='slot_name',
            field=models.CharField(blank=True, default='15 Minutes', max_length=254, null=True),
        ),
    ]
