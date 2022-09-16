""" Import Modules """
from django.contrib import admin

from .models import Booking, Slot, User, Session

class BookingAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for bookings """
    list_display = (
        'pk',
        'date',
        'time',
        # 'duration',
        'title_no',
        'date_booked',
        'user',
    )

    ordering = (
        '-pk', 'date', 'time', 'title_no', 'date_booked', 'user',
    )


class SessionAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for appointment slots """
    list_display = (
        'pk',
        'name',
        'friendly_name',
    )

    ordering = ('pk', 'name',)

class SlotAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for appointment slots """
    list_display = (
        'pk',
        # 'date',
        'name',
        # 'friendly_name',
        'session',
        'start_time',
        'end_time',
        # 'duration',
        # 'day_start',
        # 'day_finish',
        # 'title_no',
        # 'date_created',
        # 'user',
    )

    ordering = ('pk', 'start_time', 'session')


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
admin.site.register(Session, SessionAdmin)
