""" Import Modules """
from django.contrib import admin

from .models import Booking, Slot, User

class BookingAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for bookings """
    list_display = (
        'pk',
        'date',
        'time',
        # 'duration',
        'location',
        'date_booked',
        'user',
    )

    ordering = (
        '-pk', 'date', 'time', 'location', 'date_booked', 'user',
    )


class SlotAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for appointment slots """
    list_display = (
        'pk',
        'date',
        'start_time',
        'duration',
        'day_start',
        'day_finish',
        'location',
        'date_created',
        'user',
    )

    ordering = ('-pk', 'date', 'location', 'date_created', 'user',)


class UserAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for users """
    list_display = (
        'pk',
        # 'name',
        'user_name',
        'f_name',
        'l_name',
        'user_email',
        'user_phone',
        'is_active',
        'is_agent',
        'is_owner',
        'is_superuser',
    )

    ordering = (
        '-pk', 'user_name', 'l_name', 'f_name', 'is_active', 'is_agent', 'is_owner',
        'is_superuser',
        )


admin.site.register(Booking, BookingAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(User, UserAdmin)
