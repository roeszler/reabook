""" Import Modules """
from django.db import models

from app_properties.models import Property


class Booking(models.Model):
    """ To contain the data from the bookings.json fixtures file  """
    user = models.ForeignKey(
        'User', null=True, blank=True, on_delete=models.SET_NULL
        )
    duration = models.ForeignKey(
        'Slots', null=True, blank=True, on_delete=models.SET_NULL
        )
    location = models.ForeignKey(
        Property, null=True, blank=True, on_delete=models.SET_NULL
        )

    name = models.CharField(max_length=254)
    date = models.DateField()
    time = models.TimeField()
    booking_date = models.DateTimeField()

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Bookings'

    def __str__(self):
        """ Takes in the sector model to return db name """
        return self.name



class Slot(models.Model):
    """ To contain the data from the slots.json fixtures file """
    user = models.ForeignKey(
        'User', null=True, blank=True, on_delete=models.SET_NULL
        )
    location = models.ForeignKey(
        Property, null=True, blank=True, on_delete=models.SET_NULL
        )

    name = models.CharField(max_length=254)
    date = models.DateField()
    duration = models.IntegerField(default=15)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_lunch = models.TimeField(default=13)
    finish_lunch = models.TimeField(default=14)
    start_day = models.TimeField(default=9)
    finish_day = models.TimeField(default=17)
    creation_date = models.DateTimeField()



    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Slots'

    def __str__(self):
        """ Takes in the category model to return db name """
        return self.name



class User(models.Model):
    """ To contain the data from the users.json fixtures file """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    f_name = models.CharField(max_length=254)
    l_name = models.CharField(max_length=254)
    username = models.CharField(max_length=254, null=True, blank=True, unique=True)
    user_email = models.EmailField(max_length=254, unique=True)
    user_phone = models.IntegerField(max_length=19, null=True, blank=True)
    password = models.CharField(max_length=254)
    is_active = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    def __str__(self):
        """ Takes in the category model to return db name """
        return self.name

    def get_friendly_name(self):
        """ Takes in the category model to return friendly_name """
        return self.friendly_name
