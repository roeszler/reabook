""" Import Modules """
from django.db import models

# from app_properties.models import Property


class Booking(models.Model):
    """ To contain the data from the categories.json fixtures file  """

    def __str__(self):
        """ Takes in the sector model to return db name """
        return self.name

    def get_friendly_name(self):
        """ Takes in the sector model to return friendly_name """
        return self.friendly_name


class AppointmentTypes(models.Model):
    """ To contain the data from the categories.json fixtures file """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    duration = models.IntegerField(default=15)


    def __str__(self):
        """ Takes in the category model to return db name """
        return self.name

    def get_friendly_name(self):
        """ Takes in the category model to return friendly_name """
        return self.friendly_name
