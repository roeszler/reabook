""" Import Models """
from django.shortcuts import render, redirect, reverse

from app_properties.models import Property
from .models import AppointmentTypes
# from .models import Booking


def view_my_bookings(request):
    """
    View to render the bookings page
    Looks within the current directory app_bookings/templates/book/book.html
    """
    return render(request, 'book/a-bookings.html')


def view_bookings_login(request):
    """
    View to render the bookings login page
    """
    return render(request, 'book/c-booking-login.html')


def view_booking_details(request):
    """
    View to render the bookings request details page
    """
    return render(request, 'book/d-booking-details.html')


def view_booking_select_time(request):
    """
    View to render the bookings select available time page
    """
    return render(request, 'book/e-booking-select-time.html')


def view_booking_success(request):
    """
    View to render the bookings successful booking page
    """
    return render(request, 'book/f-booking-success.html')


def choose_bookings(request):
    """
    View to render the choose bookings page
    Looks within the current directory app_bookings/templates/book/book.html
    """
    properties = Property.objects.all()
    appointment_types = AppointmentTypes.objects.all()
    props_with_viewings = properties.filter(viewings=True)
    props_selected_to_view = properties.filter(selected=True)
    # appointment_duration = appointment_types.filter(duration=15)

    # select_property = request.POST.get('booking_available', False)
    # if select_property == 'on':
    #     select_property = True

    # save(update_fields=['booking_available'])
    # print('Property selected')


    context = {
        'properties': properties,
        'appointment_types': appointment_types,
        'props_with_viewings': props_with_viewings,
        'props_selected_to_view': props_selected_to_view,
        # 'appointment_duration': appointment_duration,
    }
    return render(request, 'book/b-booking-choose-property.html', context)
