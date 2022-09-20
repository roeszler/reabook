""" Import Modules """
from datetime import date, datetime
from django.db import models
from django.utils import timezone


# class Appointment(models.Model):
#     """ An individual record of the appointment to be used in the diary  """


class Booking(models.Model):
    """ An individual record of the appointment to be used in the diary  """
    client = models.ForeignKey('app_bookings.Client', null=True, blank=True, on_delete=models.SET_NULL)
    # timeslot = models.ForeignKey('app_bookings.Timeslot', null=True, blank=True, on_delete=models.SET_NULL)
    property_id = models.ForeignKey('app_properties.Property', null=True, blank=True, on_delete=models.SET_NULL)

    booking_name = models.CharField(max_length=254, null=True, blank=True, default='15min Viewing')
    date = models.DateField(default=date.today)
    date_booked = models.DateTimeField(default=timezone.now)
    viewing_active = models.BooleanField(default=True)

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Bookings'

    def __str__(self):
        """ Takes in the booking model to return db name """
        return self.booking_name


# class Session(models.Model):
#     """ TTable to contain the information about the scheldule the property is available  """
#     name = models.CharField(max_length=254, default='Morning')
#     friendly_name = models.CharField(max_length=254, null=True, blank=True)

#     class Meta:
#         """ to adjust the verbose name or the plural form from defaults """
#         verbose_name_plural = 'Sessions'

#     def __str__(self):
#         """ Takes in the category model to return db name """
#         return self.name

#     def get_friendly_name(self):
#         """ Takes in the category model to return friendly_name """
#         return self.friendly_name


# class Timeslot(models.Model):
#     """ To contain the variety of time slots available for appointments """
#     session = models.ForeignKey('Session', null=True, blank=True, on_delete=models.SET_NULL)
#     name = models.CharField(max_length=254, null=True, blank=True, default='9 to 9:15')
#     friendly_name = models.CharField(max_length=254, null=True, blank=True, default='15 min')
#     start_time = models.TimeField(default=timezone.now)
#     end_time = models.TimeField(default=timezone.now)
#     seats_available = models.IntegerField(default=3)

#     class Meta:
#         """ to adjust the slot name or the plural form from defaults """
#         verbose_name_plural = 'Timeslots'

#     def __str__(self):
#         """ Takes in the slots model to return db name """
#         # return str(self.property_id)
#         return self.name
    
#     def __int__(self):
#         """ Takes in the category model to return db name """
#         return self.pk
    
#     def get_friendly_name(self):
#         """ Takes in the booking model to return friendly_name """
#         return self.friendly_name


class Client(models.Model):
    """ To contain the data from the users.json fixtures file """
    f_name = models.CharField(max_length=254)
    l_name = models.CharField(max_length=254)
    client_username = models.CharField(max_length=254, unique=True, default='Create Username')
    client_email = models.EmailField(max_length=254, unique=True)
    client_phone = models.IntegerField(null=True, blank=True, default='00X1 123 456 789')


    def __str__(self):
        """ Takes in the user model to return db name """
        return self.client_username

    def get_friendly_name(self):
        """ Takes in the user model to return friendly_name """
        return self.client_email


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
