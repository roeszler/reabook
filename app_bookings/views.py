""" Import Models """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

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
    """ View to render the choose bookings page """
    properties = Property.objects.all()
    appointment_types = AppointmentTypes.objects.all()
    props_with_viewings = properties.filter(viewings=True)
    props_selected_to_view = properties.filter(selected=True)

    # print('props_with_viewings', props_with_viewings)
    # print('props_selected_to_view', props_selected_to_view)
    # print('properties', properties)

    query = None

    # Available viewings search function
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('choose_bookings'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ribbon_feature__icontains=query) | Q(sale_price__icontains=query) | Q(rent_pw__icontains=query) | Q(suburb__icontains=query) | Q(street__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query) | Q(country__icontains=query) | Q(postcode__icontains=query)
            props_with_viewings = props_with_viewings.filter(queries)
            # print('found q', queries)
    
    # if request.POST.get('checked', True):
    #     checked = request.get('checked')
    #     props_selected_to_view = props_selected_to_view.filter(checked)

    
    context = {
        'properties': properties,
        'appointment_types': appointment_types,
        'props_with_viewings': props_with_viewings,
        'props_selected_to_view': props_selected_to_view,
        'search_term': query,
    }
    return render(request, 'book/search-viewings.html', context)
