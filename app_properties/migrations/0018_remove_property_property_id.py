# Generated by Django 3.2.15 on 2022-09-15 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_properties', '0017_auto_20220915_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='property_id',
        ),
    ]
