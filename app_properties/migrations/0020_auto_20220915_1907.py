# Generated by Django 3.2.15 on 2022-09-15 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_properties', '0019_property_prop_id_string'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='prop_id_string',
        ),
        migrations.AlterField(
            model_name='property',
            name='title_no',
            field=models.CharField(default='LT0000', max_length=254),
        ),
    ]
