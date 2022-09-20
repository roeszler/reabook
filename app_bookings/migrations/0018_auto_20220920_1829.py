# Generated by Django 3.2.15 on 2022-09-20 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_properties', '0003_alter_property_title_no'),
        ('app_bookings', '0017_client_client_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='contact_ok',
        ),
        migrations.AddField(
            model_name='client',
            name='contact_ok',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='property_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_properties.property'),
        ),
    ]
