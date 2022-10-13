""" Import Modules """
from datetime import date
import uuid, pytz

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Booking(models.Model):
    """ An individual record of the appointment to be used in the diary  """
    booking_number = models.CharField(max_length=256, null=False, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    property_id = models.ForeignKey('app_properties.Property', null=True, blank=True, on_delete=models.SET_NULL)
    booking_name = models.CharField(max_length=254, null=True, blank=True, default='15 min Viewing')
    date_of_viewing = models.DateField(default=date.today)
    time_of_viewing = models.TimeField(default=timezone.now)
    client_message = models.TextField(null=True, blank=True, max_length=140)
    date_submitted = models.DateTimeField(auto_now_add=True)

    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    client_username = models.CharField(max_length=40, null=True, blank=True, default='Create Username')
    client_email = models.EmailField(max_length=254)
    client_phone = models.IntegerField(null=True, blank=True, default='')
    client_city = models.CharField(max_length=140, null=True, blank=True)
    client_state = models.CharField(max_length=10, null=True, blank=True)
    client_zip = models.CharField(max_length=10, blank=True,)
    client_country = models.CharField(max_length=2, choices=pytz.country_names.items(), null=True, blank=True)
    viewing_active = models.BooleanField(default=True)
    contact_ok = models.BooleanField(default=False)

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Bookings'
        # unique_together = ['f_name', 'l_name', 'client_email', 'booking_number']

    def _generate_booking_number(self):
        """ Generate a random, unique booking number using UUID """
        return uuid.uuid4().hex.upper()  # to generate a random string of 8 numbers to booking No.

    def save(self, *args, **kwargs):
        """
        To override the default save method to create the
        booking no.if it hasn't been set already.
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        # to execute the original save method
        super().save(*args, **kwargs)

    def __str__(self):
        """ Takes in the booking model to return db name """
        return self.booking_number
