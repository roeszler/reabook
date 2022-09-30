# Generated by Django 3.2.15 on 2022-09-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookings', '0005_alter_booking_client_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='client_phone',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='client_zip',
            field=models.CharField(default='', max_length=10),
        ),
    ]