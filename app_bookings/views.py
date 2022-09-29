""" Import Models """
from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail
# from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from app_properties.models import Property
from .models import Booking
from .forms import BookingForm


def add_to_diary(request, property_id):
    """ Add a quantity of the specified prop to the shopping diary """
    properties = Property.objects.all()  # noqa
    prop = get_object_or_404(Property, pk=property_id)
    diary = request.session.get('diary', {})
    props_with_viewings = properties.filter(viewings=True)
    query = None

    if request.GET:
        # Sub-query for properties available for viewing
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(pk__icontains=query) | Q(name__icontains=query) | Q(description__icontains=query) | Q(ribbon_feature__icontains=query) | Q(sale_price__icontains=query) | Q(rent_pw__icontains=query) | Q(suburb__icontains=query) | Q(street__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query) | Q(country__icontains=query) | Q(postcode__icontains=query)  # noqa
            props_with_viewings = props_with_viewings.filter(queries)

    if property_id in list(diary.keys()):
        messages.success(request, f'You already have a booking to view {prop.name} {diary[property_id]}') # noqa
    else:
        messages.success(request, f'Added {prop.name} to your appointments \
            diary')

    # update the diary variable into the session [ a python dictionary ].
    request.session['diary'] = diary

    context = {
        'prop': prop,
        'diary': diary,
    }
    return render(request, 'book/search-viewings.html', context)


def booking_detail(request, property_id):
    """ A view to show individual property booking details """
    bookings = Booking.objects.all()  # noqa
    props_with_booking_slots = bookings.filter(viewing_active=True)
    prop = get_object_or_404(Property, pk=property_id)
    booking_form = BookingForm(instance=prop)

    context = {
        'booking_form': booking_form,
        'prop': prop,
        'props_with_booking_slots': props_with_booking_slots,
    }

    return render(request, 'book/prop-booking.html', context)


def add_booking(request, property_id):
    """ View to render a successful booking on prop-booking.html """
    prop = Property.objects.get(pk=property_id)  # noqa
    booking_form = BookingForm(instance=prop)
    user = request.user

    property_id = f'{prop.id}'
    date_of_viewing = request.POST.get('date_of_viewing', 'n/p')
    time_of_viewing = request.POST.get('time_of_viewing', 'n/p')
    f_name = request.POST['f_name']
    l_name = request.POST['l_name']
    client_email = request.POST['client_email']
    client_country = request.POST.get('client_country', 'n/p')
    client_phone = request.POST['client_phone']
    client_city = request.POST['client_city']
    client_zip = request.POST['client_zip']
    client_message = request.POST['client_message']
    date_submitted = datetime.now()
    contact_ok = request.POST.get('contact_ok')

    context = {
        'prop': prop,
        'user': user,
        'booking_form': booking_form,
        'property_id': property_id,
        'date_of_viewing': date_of_viewing,
        'time_of_viewing': time_of_viewing,
        'f_name': f_name,
        'l_name': l_name,
        'client_email': client_email,
        'client_country': client_country,
        'client_phone': client_phone,
        'client_city': client_city,
        'client_zip': client_zip,
        'client_message': client_message,
        'date_submitted': date_submitted,
        'contact_ok': contact_ok,
    }

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_f = booking_form.save(commit=False)
            booking_f.user = request.user
            booking_f.property_id = prop
            booking_f.save()
            print('Booking information has been saved')

            # Send an email
            send_mail(
                'Message from ' + f_name + l_name + ' at ' + client_email + '\
                    , regarding: ' + property_id,
                'Property: ' + property_id + ', Date and time of proposed \
                viewing: ' + date_of_viewing + ' at ' + time_of_viewing + '\
                , Message: ' + client_message, client_email, ['\
                bookings@reabook.net', 'someone@realestateagent\
                customer.com', client_email, ]
            )
        else:
            messages.error(
                    request, 'We have a problem. Please check you \
                        have entered all time, date and booking fields.'
                    )
            return render(request, 'book/prop-booking.html', context)

        return render(request, 'book/booking-success.html', context)


def choose_bookings(request):
    """ View to render the choose bookings page """
    properties = Property.objects.all() # noqa
    props_with_viewings = properties.filter(viewings=True)

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
        'props_with_viewings': props_with_viewings,
        'search_term': query,
    }
    return render(request, 'book/search-viewings.html', context)


def my_diary(request, user_id):
    """ To list all the users bookings in the DB """
    prop = Property.objects.all() # noqa
    bookings = Booking.objects.all() # noqa
    user = get_object_or_404(User, pk=user_id)

    context = {
        'bookings': bookings,
        'prop': prop,
        'user': user,
        }
    return render(request, 'book/my-diary.html', context)


def parked(request):
    """ View to render the bookings the parked page """
    return render(request, 'book/parked.html')


def update_booking(request, booking_id):
    """ To update the bookings made by each user """
    booking = Booking.objects.get(pk=booking_id) # noqa
    booking_form = BookingForm(request.POST or None, instance=booking)

    context = {
        'booking_form': booking_form,
        'booking': booking,
        }
    return render(request, 'book/update-booking.html', context)
