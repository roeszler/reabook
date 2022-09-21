""" Import Modules """
import uuid

from datetime import date, datetime
from django import forms
from django.db import models
from django.utils import timezone


class Booking(models.Model):
    """ An individual record of the appointment to be used in the diary  """
    booking_number = models.CharField(max_length=8, null=False, editable=False)
    client = models.ForeignKey('app_bookings.Client', null=True, on_delete=models.SET_NULL)
    property_id = models.ForeignKey('app_properties.Property', null=True, blank=True, on_delete=models.SET_NULL)
    booking_name = models.CharField(max_length=254, null=True, blank=True, default='15 min Viewing')
    date_of_viewing = models.DateField(default=date.today)
    time_of_viewing = models.TimeField(default=timezone.now)
    client_message = models.TextField(null=True, blank=True)
    date_submitted = models.DateTimeField(default=timezone.now)
    viewing_active = models.BooleanField(default=True)

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Bookings'

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


class Client(models.Model):
    """ To contain the data from the users.json fixtures file """
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    client_username = models.CharField(max_length=40, default='Create Username')
    client_email = models.EmailField(max_length=254)
    client_phone = models.IntegerField(null=True, blank=True, default=123456789)
    client_city = models.CharField(max_length=140, null=True, blank=True)
    client_state = models.CharField(max_length=10, null=True, blank=True)
    client_zip = models.CharField(max_length=10, default='123 45')
    client_country = models.CharField(max_length=140, null=True, blank=True)
    contact_ok = models.BooleanField(default=True)
    # contact_ok = True if forms.CheckboxInput("status") == "on" else False
    # contact_ok = forms.CheckboxInput()
    # contact_ok = forms.CheckboxInput(True if "status" == "on" else False)

    def __str__(self):
        """ Takes in the user model to return db name """
        # return self.client_email
        return f"{self.id} - {self.f_name} {self.l_name}"

    def get_friendly_name(self):
        """ Takes in the user model to return friendly_name """
        return self.client_username


class BookViewingTime(models.Model):
    """ To contain the data from user bookings """
    booking_number = models.CharField(max_length=8, null=False, editable=False)
    client = models.ForeignKey('app_bookings.Client', null=True, on_delete=models.SET_NULL)
    property_id = models.ForeignKey('app_properties.Property', null=True, blank=True, on_delete=models.SET_NULL)
    booking_name = models.CharField(max_length=254, null=True, blank=True, default='15 min Viewing')
    date_of_viewing = models.DateField(default=date.today)
    time_of_viewing = models.TimeField(default=timezone.now)
    client_message = models.TextField(null=True, blank=True)
    date_submitted = models.DateTimeField(default=timezone.now)
    viewing_active = models.BooleanField(default=True)
    f_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    client_username = models.CharField(max_length=40, default='Create Username')
    client_email = models.EmailField(max_length=254)
    client_phone = models.IntegerField(null=True, blank=True, default=123456789)
    client_city = models.CharField(max_length=140, null=True, blank=True)
    client_state = models.CharField(max_length=10, null=True, blank=True)
    client_zip = models.CharField(max_length=10, default='123 45')
    client_country = models.CharField(max_length=140, null=True, blank=True)
    contact_ok = models.BooleanField(default=True)

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Bookings'

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


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
