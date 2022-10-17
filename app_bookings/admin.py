""" Import Modules """
from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for bookings """
    list_display = (
        'pk',
        'property_id',
        'client_email',
        'f_name',
        'l_name',
        'client_phone',
        'user',
        'date_of_viewing',
        'time_of_viewing',
        'date_submitted',
        'contact_ok',
        'client_message',
        'viewing_active',
    )

    ordering = (
        '-pk', 'date_of_viewing', 'time_of_viewing', 'property_id',
        'date_submitted',
    )
