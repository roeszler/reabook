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
    properties = Property.objects.all() # noqa
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
    bookings = Booking.objects.all()  # noqa
    props_with_booking_slots = bookings.filter(viewing_active=True)
    prop = get_object_or_404(Property, pk=property_id)
    booking_form = BookingForm(instance=prop)
    user = request.user
    users_bookings = Booking.objects.filter(user=user) # noqa

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
    prop = Property.objects.get(pk=property_id)  # noqa
    booking_form = BookingForm(instance=prop)
    user = request.user
    users_bookings = Booking.objects.filter(user=user) # noqa

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
    properties = Property.objects.all() # noqa
    props_with_viewings = properties.filter(viewings=True)
    user = request.user
    users_bookings = Booking.objects.filter(user=user) # noqa
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

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ribbon_feature__icontains=query) | Q(sale_price__icontains=query) | Q(rent_pw__icontains=query) | Q(suburb__icontains=query) | Q(street__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query) | Q(country__icontains=query) | Q(postcode__icontains=query) # noqa
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

    if user.is_authenticated:
        users_bookings = Booking.objects.filter(user=user) # noqa
        bookings_count = users_bookings.count()
        request.session['bookings_count'] = users_bookings.count()
    else:
        bookings_count = 0

    context = {
        'users_bookings': users_bookings,
        'prop': prop,
        'user': user,
        'bookings_count': bookings_count,
        }
    return render(request, 'book/my-diary.html', context)


@login_required
def update_booking(request, booking_id):
    """ To update the bookings made by each user """
    booking = Booking.objects.get(pk=booking_id) # noqa
    booking_form = BookingForm(instance=booking)
    user = request.user
    users_bookings = Booking.objects.filter(user=user) # noqa
    property_id = booking.property_id

    if booking.user == request.user:
        if request.method == 'POST':
            booking_form = BookingForm(request.POST, instance=booking)
            if booking_form.is_valid():
                book_f = booking_form.save(False)
                book_f.user = request.user
                book_f.client_zip = booking.client_zip
                book_f.property_id = property_id
                book_f.save()

                # Send an email
                send_mail(
                    f'UPDATE Reabook appointment request: {user.email} - for\
                        booking no.{booking_id}',
                    f'Property: {book_f.property_id}\n\
                        Address:\n\
                        {book_f.property_id.house_no} \
                            {book_f.property_id.street}\n\
                        {book_f.property_id.suburb} \
                            {book_f.property_id.postcode}\n\
                        User  {booking.f_name} {booking.l_name}.\n\
                        Email: {booking.client_email}\n\
                        Proposed time: {booking.time_of_viewing}\n\
                        Proposed date: {booking.date_of_viewing}\n\
                        Additional: {booking.client_message}\n\
                        User id. {user.id}\n',
                    'bookings@reabook.net',
                    ['viewings@reabook.net', 'agent@example.com\
                        ', book_f.property_id.realtor.email,
                        booking.client_email, ],
                    fail_silently=False,
                )

                print('Edit to your booking request has been saved')
                messages.success(request, f'Booking request id.{booking_id}\
                    has been updated and an email sent to the Managing Agent')
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
        print(f'booking.user: {booking.user.id}')
        print(f'request.user: {request.user.id}')
        messages.success(request, f'Booking id.{booking_id} deleted!')
        return redirect(f'/book/diary/{user.id}/')


def integer_type_check(request):
    """ To ensure that only an integer is entered into a field """
    if isinstance(request, int):
        return True
    else:
        raise TypeError('An integer was not passed into the field')

    if __name__ == '__main__':
        print(integer_type_check(10))


def parked(request):
    """ View to render the bookings the parked page """
    user = request.user
    users_bookings = Booking.objects.filter(user=user) # noqa

    return render(request, 'book/parked.html', {'users_bookings': users_bookings, }) # noqa
