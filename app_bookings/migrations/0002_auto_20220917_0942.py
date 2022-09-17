# Generated by Django 3.2.15 on 2022-09-17 09:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=254)),
                ('l_name', models.CharField(max_length=254)),
                ('client_username', models.CharField(default='Create Username', max_length=254, unique=True)),
                ('client_email', models.EmailField(max_length=254, unique=True)),
                ('client_phone', models.IntegerField(blank=True, default='00X1 123 456 789', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='9 to 9:15', max_length=254, null=True)),
                ('friendly_name', models.CharField(blank=True, default='15 min', max_length=254, null=True)),
                ('start_time', models.TimeField(default=django.utils.timezone.now)),
                ('end_time', models.TimeField(default=django.utils.timezone.now)),
                ('seats_available', models.IntegerField(default=3)),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_bookings.session')),
            ],
            options={
                'verbose_name_plural': 'Timeslots',
            },
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name_plural': 'Assign Slots to Properties'},
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='title_no',
            new_name='property_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='appointment_slot',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='viewing_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_name',
            field=models.CharField(blank=True, default='ReaBook 15 Minute Property Viewing', max_length=254, null=True),
        ),
        migrations.DeleteModel(
            name='Slot',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='booking',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_bookings.client'),
        ),
        migrations.AddField(
            model_name='booking',
            name='timeslot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_bookings.timeslot'),
        ),
    ]