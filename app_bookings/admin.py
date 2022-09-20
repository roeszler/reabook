""" Import Modules """
from django.contrib import admin

from .models import Booking, Client, Question, Choice


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for bookings """
    list_display = (
        'pk',
        'property_id',
        'client',
        'booking_name',
        'date_of_viewing',
        'time_of_viewing',
        'client_message',
        'date_booked',
        'viewing_active',
    )

    ordering = (
        '-pk', 'date_of_viewing', 'time_of_viewing', 'property_id', 'client', 'date_booked',
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for users """
    list_display = (
        'pk',
        'f_name',
        'l_name',
        'client_username',
        'client_email',
        'client_phone',
        'client_city',
        'client_zip',
        'client_country',
        'contact_ok',
    )

    ordering = (
        '-pk', 'client_username', 'l_name', 'f_name', 'client_email',
        'client_phone',
        )


admin.site.register(Question)
admin.site.register(Choice)
# admin.site.register(Booking, BookingAdmin)
# admin.site.register(Timeslot, TimeslotAdmin)
# admin.site.register(Client, ClientAdmin)
# admin.site.register(Session, SessionAdmin)
