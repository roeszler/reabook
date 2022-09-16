""" Import Modules """
from datetime import date
from django.db import models
from django.utils import timezone
from django import forms

# from app_properties.models import Property
from .forms import GeeksForm


class Booking(models.Model):
    """ To contain the data from the bookings.json fixtures file  """
    user = models.ForeignKey(
        'app_bookings.User', null=True, blank=True, on_delete=models.SET_NULL
        )
    appointment_slot = models.ForeignKey(
        'app_bookings.Slot', null=True, blank=True, on_delete=models.SET_NULL
        )
    title_no = models.ForeignKey(
        'app_properties.Property', null=True, blank=True, on_delete=models.SET_NULL
        )
    # property_id = models.CharField(Property, 'title_no', max_length=254)
    booking_name = models.CharField(max_length=254, null=True, blank=True, default='ReaBook 15 Minute Property Viewing Appointment')
    date = models.DateField(default=date.today)
    time = models.TimeField(default=timezone.now)
    date_booked = models.DateTimeField(default=timezone.now)

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Bookings'

    def __str__(self):
        """ Takes in the booking model to return db name """
        return self.booking_name


class Session(models.Model):
    """ To contain the data from the categories.json fixtures file  """
    name = models.CharField(max_length=254, default='Morning')
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Sessions'

    def __str__(self):
        """ Takes in the category model to return db name """
        return self.name

    def get_friendly_name(self):
        """ Takes in the category model to return friendly_name """
        return self.friendly_name


class Slot(models.Model):
    """ To contain the appointment slots data from slots.json """
    # user = models.ForeignKey(
    #     'User', null=True, blank=True, on_delete=models.SET_NULL
    #     )
    # title_no = models.ForeignKey(
    #     Property, null=True, blank=True, on_delete=models.SET_NULL
    #     )
    session = models.ForeignKey(
        'Session', null=True, blank=True, on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=254, null=True, blank=True, default='9 to 9:15')
    friendly_name = models.CharField(max_length=254, null=True, blank=True, default='9 to 9:15 Appointment Slot')
    # session_morning = models.BooleanField(null=True, blank=True, default=True)
    # session_morning = forms.ChoiceField(choices=GeeksForm, widget=forms.RadioSelect())
    # date = models.DateField(default=timezone.now)
    # duration = models.DurationField(default='00:15')
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    # lunch_start = models.TimeField(default='13:00')
    # lunch_finish = models.TimeField(default='14:00')
    # day_start = models.TimeField(default='09:00')
    # day_finish = models.TimeField(default='17:00')
    # date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        """ to adjust the slot name or the plural form from defaults """
        verbose_name_plural = 'Appointment Slots'

    def __str__(self):
        """ Takes in the slots model to return db name """
        # return str(self.property_id)
        return self.name
    
    def __int__(self):
        """ Takes in the category model to return db name """
        return self.pk
    
    def get_friendly_name(self):
        """ Takes in the booking model to return friendly_name """
        return self.friendly_name



class User(models.Model):
    """ To contain the data from the users.json fixtures file """
    # user_data = models.CharField(max_length=254, null=True, blank=True, default='Admin')
    f_name = models.CharField(max_length=254)
    l_name = models.CharField(max_length=254)
    # friendly_name = models.CharField(max_length=254, null=True, blank=True default='')
    user_name = models.CharField(max_length=254, unique=True, default='Create Username')
    user_email = models.EmailField(max_length=254, unique=True)
    user_phone = models.IntegerField(null=True, blank=True, default='00X1 123 456 789')
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
