# Generated by Django 3.2.15 on 2022-09-20 08:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookings', '0006_auto_20220920_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='date_of_viewing',
        ),
        migrations.AddField(
            model_name='booking',
            name='client_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='contact_ok',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='client',
            name='client_city',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='client_country',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='client_zip',
            field=models.CharField(default='123 45', max_length=140),
        ),
    ]
