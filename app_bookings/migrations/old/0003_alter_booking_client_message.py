# Generated by Django 3.2.15 on 2022-09-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookings', '0002_remove_booking_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='client_message',
            field=models.TextField(blank=True, max_length=140, null=True),
        ),
    ]