# Generated by Django 3.2.15 on 2022-09-13 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name_plural': 'Bookings'},
        ),
    ]