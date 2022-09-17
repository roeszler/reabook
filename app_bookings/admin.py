""" Import Modules """
from django.contrib import admin

from .models import Booking, Timeslot, Client, Session


class BookingAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for bookings """
    list_display = (
        'pk',
        'property_id',
        'date',
        'timeslot',
        'client',
        'date_booked',
        'viewing_active',
    )

    ordering = (
        '-pk', 'date', 'timeslot', 'property_id', 'client',
    )


class SessionAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for appointment slots """
    list_display = (
        'pk',
        'name',
        'friendly_name',
    )

    ordering = ('pk', 'name',)

class TimeslotAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for appointment slots """
    list_display = (
        'pk',
        'name',
        'session',
        'start_time',
        'end_time',
        'seats_available',
    )

    ordering = ('pk', 'start_time', 'session')


class ClientAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for users """
    list_display = (
        'pk',
        'f_name',
        'l_name',
        'client_username',
        'client_email',
        'client_phone'
    )

    ordering = (
        '-pk', 'client_username', 'l_name', 'f_name', 'client_email',
        'client_phone',
        )


admin.site.register(Booking, BookingAdmin)
admin.site.register(Timeslot, TimeslotAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Session, SessionAdmin)
