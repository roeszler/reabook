# Generated by Django 3.2.15 on 2022-09-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookings', '0007_auto_20220927_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='viewing_active',
            field=models.BooleanField(default=False),
        ),
    ]