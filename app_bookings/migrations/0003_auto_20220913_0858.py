# Generated by Django 3.2.15 on 2022-09-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookings', '0002_alter_booking_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='prop_viewing_booked', max_length=254),
        ),
    ]