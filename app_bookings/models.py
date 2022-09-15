""" Import Modules """
from datetime import date
from django.db import models
from django.utils import timezone

from app_properties.models import Property


class Booking(models.Model):
    """ To contain the data from the bookings.json fixtures file  """
    user = models.ForeignKey(
        'app_bookings.User', null=True, blank=True, on_delete=models.SET_NULL
        )
    duration = models.ForeignKey(
        'app_bookings.Slot', null=True, blank=True, on_delete=models.SET_NULL
        )
    location = models.ForeignKey(
        'app_properties.Property', null=True, blank=True, on_delete=models.SET_NULL
        )
    booking_name = models.CharField(max_length=254, null=True, blank=True, default='booking_data')
    date = models.DateField(default=date.today)
    time = models.TimeField(default=timezone.now)
    date_booked = models.DateTimeField(default=timezone.now)

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Bookings'

    def __str__(self):
        """ Takes in the sector model to return db name """
        return self.booking_name



class Slot(models.Model):
    """ To contain the data from the slots.json fixtures file """
    user = models.ForeignKey(
        'User', null=True, blank=True, on_delete=models.SET_NULL
        )
    location = models.ForeignKey(
        Property, null=True, blank=True, on_delete=models.SET_NULL
        )

    slot_name = models.CharField(max_length=254, null=True, blank=True, default='ReaBook 15 Minute Property Viewing Appointment')
    date = models.DateField()
    duration = models.TimeField(default='00:15')
    start_time = models.TimeField()
    end_time = models.TimeField()
    lunch_start = models.TimeField(default='13:00:00')
    lunch_finish = models.TimeField(default='14:00:00')
    day_start = models.TimeField(default='09:00:00')
    day_finish = models.TimeField(default='17:00:00')
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Slots'

    def __str__(self):
        """ Takes in the category model to return db name """
        return self.slot_name



class User(models.Model):
    """ To contain the data from the users.json fixtures file """
    user_data = models.CharField(max_length=254, null=True, blank=True, default='user_data')
    f_name = models.CharField(max_length=254)
    l_name = models.CharField(max_length=254)
    # friendly_name = models.CharField(max_length=254, null=True, blank=True default='')
    user_name = models.CharField(max_length=254, unique=True, default='Create Username')
    user_email = models.EmailField(max_length=254, unique=True)
    user_phone = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=254)
    is_active = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    def __str__(self):
        """ Takes in the user model to return db name """
        return self.user_name

    def get_friendly_name(self):
        """ Takes in the user model to return friendly_name """
        return self.user_email
