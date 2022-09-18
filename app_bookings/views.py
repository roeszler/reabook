""" Import Models """
from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from app_properties.models import Property
from .models import Timeslot, Booking
# from .models import Booking


def client_bookings(request):
    """ To render the bookings page with clients upcoming appointments """
    return render(request, 'book/my-bookings.html', {})

def booking_success(request):
    """ View to render a successful booking on prop-booking-detail.html """

    if request.method == 'POST':

        form_data = {
            # 'property_id': request.POST['property_id'],
            'date': request.POST['date'],
            # 'time': request.POST['time'],
            'f_name': request.POST['f_name'],
            'l_name': request.POST['l_name'],
            'client_email': request.POST['client_email'],
            'continent_code': request.POST['continent_code'],
            'client_phone': request.POST['client_phone'],
            'client_city': request.POST['client_city'],
            'client_zip': request.POST['client_zip'],
            # 'client_country': request.POST['client_country'],
            'client_message': request.POST['client_message'],
            'date_submitted': datetime.now(),
        }

        print(form_data)
        # print(date_booked)
        return render(request, 'book/booking-success.html', form_data)
    else:
        return render(request, 'book/booking-success.html')


def view_bookings_login(request):
    """
    View to render the bookings login page
    """
    return render(request, 'book/c-booking-login.html')


def booking_detail(request, property_id):
    """ A view to show individual property booking details """
    properties = Property.objects.all() # noqa
    slots = Timeslot.objects.all() # noqa
    bookings = Booking.objects.all() # noqa
    prop = get_object_or_404(Property, pk=property_id)
    props_with_booking_slots = bookings.filter(viewing_active=True)

    context = {
        'properties': properties,
        'slots': slots,
        'bookings': bookings,
        'prop': prop,
        'props_with_booking_slots': props_with_booking_slots,
    }

    return render(request, 'book/prop-booking-detail.html', context)


# def view_booking_select_time(request):
    """
    View to render the bookings select available time page
    """
    properties = Property.objects.all() # noqa
    props_with_viewings = properties.filter(viewings=True)

    context = {
        'properties': properties,
        'props_with_viewings': props_with_viewings,
    }

    return render(request, 'book/booking-detail.html', context)


def add_to_diary(request, property_id):
    """ Add a quantity of the specified prop to the shopping diary """
    properties = Property.objects.all()
    prop = get_object_or_404(Property, pk=property_id)
    diary = request.session.get('diary', {})
    props_with_viewings = properties.filter(viewings=True)
    query = None

    if request.GET:
        # Sub-query for properties available for viewing
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(pk__icontains=query) | Q(name__icontains=query) | Q(description__icontains=query) | Q(ribbon_feature__icontains=query) | Q(sale_price__icontains=query) | Q(rent_pw__icontains=query) | Q(suburb__icontains=query) | Q(street__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query) | Q(country__icontains=query) | Q(postcode__icontains=query)
            props_with_viewings = props_with_viewings.filter(queries)

    if property_id in list(diary.keys()):
        messages.success(request, f'You already have a booking to view {prop.name} {diary[property_id]}')
    else:
        messages.success(request, f'Added {prop.name} to your shopping diary')
    
    # update the diary variable into the session [ a python dictionary ].
    request.session['diary'] = diary

    context = {
        'prop': prop,
        'diary': diary,
    }
    return render(request, 'book/search-viewings.html', context)


def choose_bookings(request):
    """ View to render the choose bookings page """
    properties = Property.objects.all()
    appointment_slot = Timeslot.objects.all()
    props_with_viewings = properties.filter(viewings=True)

    # props_selected_to_view = properties.filter(selected=True)
    # print('props_with_viewings', props_with_viewings)
    # print('props_selected_to_view', props_selected_to_view)
    # print('properties', properties)

    query = None

    # Available viewings search function
    if request.GET:

        # Sub-query for properties available for viewing
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

    context = {
        'properties': properties,
        'appointment_slot': appointment_slot,
        'props_with_viewings': props_with_viewings,
        'search_term': query,
    }
    return render(request, 'book/search-viewings.html', context)
