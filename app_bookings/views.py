""" Import Models """
from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from app_properties.models import Property
from .models import Booking
from .forms import BookingForm


@login_required
def add_to_diary(request, property_id):
    """ Add a quantity of the specified prop to the shopping diary """
    # properties = Property.objects.all()  # noqa
    properties = get_object_or_404(Property, all)
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


@login_required
def booking_detail(request, property_id):
    """ A view to show individual property booking details """
    # bookings = Booking.objects.all()  # noqa
    bookings = get_object_or_404(Booking, all)
    props_with_booking_slots = bookings.filter(viewing_active=True)
    prop = get_object_or_404(Property, pk=property_id)
    booking_form = BookingForm(instance=prop)
    user = request.user
    users_bookings = bookings.objects.filter(user=user) # noqa

    context = {
        'booking_form': booking_form,
        'users_bookings': users_bookings,
        'prop': prop,
        'user': user,
        'props_with_booking_slots': props_with_booking_slots,
    }

    return render(request, 'book/prop-booking.html', context)


@login_required
def add_booking(request, property_id):
    """ View to render a successful booking on prop-booking.html """
    # prop = Property.objects.get(pk=property_id)  # noqa
    prop = get_object_or_404(Property, pk=property_id)
    booking_form = BookingForm(instance=prop)
    user = request.user
    bookings = get_object_or_404(Booking, all)
    users_bookings = bookings.objects.filter(user=user) # noqa

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
        'users_bookings': users_bookings,
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
                f'Reabook viewing request: {client_email} - for prop\
                    .{property_id}',
                f'Property: {property_id}\n\
                    User  {f_name}  {l_name}.\n\
                    Email: {client_email}\n\
                    Proposed time: {time_of_viewing}\n\
                    Proposed date: {date_of_viewing}\n\
                    Additional: {client_message}\n\
                    User id. {user.id}\n',
                'bookings@reabook.net',
                ['viewings@reabook.net', 'agent@example.com\
                    ', prop.realtor.email, client_email, ],
                fail_silently=False,
            )
        else:
            messages.error(
                    request, 'We have a problem. Please check you \
                        have entered all time, date and booking fields.'
                    )
            print(booking_form.errors)
            return render(request, 'book/prop-booking.html', context)

        return render(request, 'book/booking-success.html', context)


@login_required
def choose_bookings(request):
    """ View to render the choose bookings page """
    # properties = Property.objects.all() # noqa
    properties = get_object_or_404(Property, all)
    bookings = get_object_or_404(Booking, all)
    props_with_viewings = properties.filter(viewings=True)
    user = request.user
    users_bookings = bookings.objects.filter(user=user) # noqa

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

    context = {
        'properties': properties,
        'props_with_viewings': props_with_viewings,
        'users_bookings': users_bookings,
        'search_term': query,
    }
    return render(request, 'book/search-viewings.html', context)


@login_required
def my_diary(request, user_id):
    """ To list all the users bookings in the DB """
    prop = Property.objects.all() # noqa
    bookings = Booking.objects.all() # noqa
    users_bookings = bookings.filter(user=user_id)
    user = get_object_or_404(User, pk=user_id)

    context = {
        'users_bookings': users_bookings,
        'prop': prop,
        'user': user,
        }
    return render(request, 'book/my-diary.html', context)


def parked(request):
    """ View to render the bookings the parked page """
    bookings = get_object_or_404(Booking, all)
    user = request.user
    users_bookings = bookings.objects.filter(user=user) # noqa

    return render(request, 'book/parked.html', {'users_bookings': users_bookings, })


@login_required
def update_booking(request, booking_id):
    """ To update the bookings made by each user """
    booking = Booking.objects.get(pk=booking_id) # noqa
    # bookings = get_object_or_404(Booking, all)
    booking_form = BookingForm(instance=booking)
    user = request.user
    users_bookings = Booking.objects.filter(user=user) # noqa

    if booking.user == request.user:
        if request.method == 'POST':
            booking_form = BookingForm(request.POST, instance=booking)
            if booking_form.is_valid():
                book_f = booking_form.save(False)
                book_f.user = request.user
                book_f.client_zip = booking.client_zip
                book_f.save()

                # Send an email
                send_mail(
                    f'UPDATE Reabook appointment request: {user.email} - for\
                        booking no.{booking_id}',
                    f'Property: {booking.property_id}\n\
                        User  {f_name}  {l_name}.\n\
                        Email: {client_email}\n\
                        Proposed time: {time_of_viewing}\n\
                        Proposed date: {date_of_viewing}\n\
                        Additional: {client_message}\n\
                        User id. {user.id}\n',
                    'bookings@reabook.net',
                    ['viewings@reabook.net', 'agent@example.com\
                        ', booking.property_id.realtor.email, booking.client_email, ],
                    fail_silently=False,
                )

                print('Edit to your booking request has been saved')
                messages.success(request, f'Booking request id.{booking_id} has\
                    been updated and an email sent to the Managing Agent')
            else:
                messages.error(request, 'Sorry, there has been an error in\
                     updating your booking details')
                print(booking_form.errors)
    else:
        messages.error(request, 'You do not have permission to update this\
             booking')

    context = {
        'booking_form': booking_form,
        'users_bookings': users_bookings,
        'booking': booking,
        }
    return render(request, 'book/update-booking.html', context)


@login_required
def delete_booking(request, booking_id):
    """ A view to authorize and manage the delete property events """
    booking = get_object_or_404(Booking, pk=booking_id)
    user = request.user

    if booking.user != request.user:
        messages.error(request, 'Sorry, only booking owners can do that.')
        return redirect(reverse('user-diary'))
    else:
        # booking.delete()
        print(f'Booking id.{booking_id} Deleted')
        messages.success(request, f'Booking id.{booking_id} deleted!')
        return redirect(f'/book/diary/{user.id}/')
