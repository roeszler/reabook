""" Import Modules """
from django.db import models

# from app_properties.models import Property


# class Booking(models.Model):
#     """ To contain the data from the categories.json fixtures file  """
#     name = models.CharField(max_length=254)
#     friendly_name = models.CharField(max_length=254, null=True, blank=True)
#     booking_available = models.BooleanField(default=False)

#     user = models.ForeignKey(
#         'User', null=True, blank=True, on_delete=models.SET_NULL
#         )
#     appointment_type = models.ForeignKey(
#         'AppointmentType', null=True, blank=True, on_delete=models.SET_NULL
#         )
#     # prop = models.ForeignKey(
#     #     'Property', null=True, blank=True, on_delete=models.SET_NULL
#     #     )

#     booking_id = models.CharField(max_length=24)
#     appointment_date = models.DateField()
#     appointment_time = models.TextField()

#     class Meta:
#         """ to adjust the verbose name or the plural form from defaults """
#         verbose_name_plural = 'Bookings'

#     def __str__(self):
#         """ Takes in the category model to return db name """
#         return self.name

#     def get_friendly_name(self):
#         """ Takes in the category model to return friendly_name """
#         return self.friendly_name


# class User(models.Model):
#     """ To contain the data from the categories.json fixtures file  """
#     name = models.CharField(max_length=254)
#     friendly_name = models.CharField(max_length=254, null=True, blank=True)

#     class Meta:
#         """ to adjust the verbose name or the plural form from defaults """
#         verbose_name_plural = 'Bookings'

#     def __str__(self):
#         """ Takes in the category model to return db name """
#         return self.name

#     def get_friendly_name(self):
#         """ Takes in the category model to return friendly_name """
#         return self.friendly_name


# class AppointmentType(models.Model):
#     """ To contain the data from the categories.json fixtures file  """
#     name = models.CharField(max_length=254)
#     friendly_name = models.CharField(max_length=254, null=True, blank=True)

#     class Meta:
#         """ to adjust the verbose name or the plural form from defaults """
#         verbose_name_plural = 'Bookings'

#     def __str__(self):
#         """ Takes in the category model to return db name """
#         return self.name

#     def get_friendly_name(self):
#         """ Takes in the category model to return friendly_name """
#         return self.friendly_name
