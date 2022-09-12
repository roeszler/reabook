""" Import Models """
from django.shortcuts import render, redirect, reverse

from app_properties.models import Property
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
    props_available_to_view = properties.filter(viewings=True)

    # select_property = request.POST.get('booking_available', False)
    # if select_property == 'on':
    #     select_property = True

    # save(update_fields=['booking_available'])
    # print('Propery selected')

    # Retrieves a single instance of a property in the DB
    prop1 = properties.get(pk=1)
    prop2 = properties.get(pk=2)
    prop3 = properties.get(pk=3)
    prop4 = properties.get(pk=4)
    prop5 = properties.get(pk=5)
    prop6 = properties.get(pk=6)

    context = {
        'properties': properties,
        'props_available_to_view': props_available_to_view,

        'prop1': prop1,
        'prop2': prop2,
        'prop3': prop3,
        'prop4': prop4,
        'prop5': prop5,
        'prop6': prop6,
    }
    return render(request, 'book/b-booking-choose-property.html', context)


# def view_bookings_home(request):
#     """
#     View to render the bookings home page
#     Looks within the current directory app_bookings/templates/book/book.html
#     """
#     properties = Property.objects.all()

#     # Retrieves a single instance of a property in the DB
#     prop1 = Property.objects.get(pk=1)
#     prop2 = Property.objects.get(pk=2)
#     prop3 = Property.objects.get(pk=3)
#     prop4 = Property.objects.get(pk=4)
#     prop5 = Property.objects.get(pk=5)

#     context = {
#         'properties': properties,
#         'prop1': prop1,
#         'prop2': prop2,
#         'prop3': prop3,
#         'prop4': prop4,
#         'prop5': prop5,
#     }
#     return render(request, 'book/a-bookings.html', context)
