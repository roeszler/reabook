""" Import Models """
from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail
# from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User

from app_properties.models import Property
from .models import Booking, Client
from .forms import BookingForm


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
        messages.success(request, f'Added {prop.name} to your appointments diary')
    
    # update the diary variable into the session [ a python dictionary ].
    request.session['diary'] = diary

    context = {
        'prop': prop,
        'diary': diary,
    }
    return render(request, 'book/search-viewings.html', context)


def booking_detail(request, property_id):
    """ A view to show individual property booking details """
    bookings = Booking.objects.all() # noqa
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
    prop = Property.objects.get(pk=property_id)
    booking_form = BookingForm(instance=prop)
    # booking = Booking.objects.get(property_id=prop)
    # latest_booking = booking.get_latest_by('date_submitted')

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_f = booking_form.save(commit=False)
            booking_f.user = request.user
            booking_f.property_id = prop
            # booking_f.save()
            # obj = booking_f.save()
            # print(obj.id)
            # print(f'{obj.id}')
            print('Booking information has been saved')
            print(property_id)
            print(booking_form.errors)

        context = {
            'prop': prop,
            # 'booking': booking,
            # 'latest_booking': latest_booking,
            'booking_form': booking_form,
        }
        return render(request, 'book/booking-success.html', context)
    
    # else:
    #     return render(request, 'book/prop-booking.html', context)
        # messages



# def old_booking_success(request, property_id):
#     """ View to render a successful booking on prop-booking.html """
#     prop = Property.objects.get(pk=property_id)
#     booking_form = BookingForm(instance=prop)
#     # booking = Booking.objects.get(pk=booking_id)
#     # user = User.objects.all()
    
#     if request.method == 'POST':
#         booking_form = BookingForm(request.POST)
#         property_id = f'{prop.id}'
#         date_of_viewing = request.POST['date']
#         time_of_viewing = request.POST.get('time', 'n/p')
#         f_name = request.POST['f_name']
#         l_name = request.POST['l_name']
#         client_email = request.POST['client_email']
#         client_country = request.POST.get('client_country', 'n/p')
#         client_phone = request.POST['client_phone']
#         client_city = request.POST['client_city']
#         client_zip = request.POST['client_zip']
#         client_message = request.POST['client_message']
#         date_submitted = datetime.now()
#         contact_ok = request.POST.get('contact_ok')
        
#         # Turn HTML based "on" into a 'TRUE' or 'FALSE' as required by Django
#         if contact_ok == 'on':
#             contact_ok = True
#         else:
#             contact_ok = False

#         booking_ins = Booking(
#             property_id=prop,
#             date_of_viewing=date_of_viewing,
#             time_of_viewing=time_of_viewing,
#             client_message=client_message,
#             date_submitted=date_submitted,
#             f_name=f_name,
#             l_name=l_name,
#             client_email=client_email,
#             client_phone=client_phone,
#             client_city=client_city,
#             client_zip=client_zip,
#             client_country=client_country,
#             contact_ok=contact_ok,
#             )
            
#         booking_ins.save()
#         print('Booking information has been saved')

#         # Send an email
#         send_mail(
#             'Message from ' + f_name + l_name + ' at ' + client_email + ', regarding: ' + property_id,
#             'Property: '+property_id+', Date and time of proposed viewing: ' +date_of_viewing+' at ' +time_of_viewing+ ', Message:' +client_message,
#             client_email,
#             ['bookings@reabook.net', 'someone@realestateagentcustomer.com', client_email, ] # to email address
#         )

#         context = {
#             'booking_form': booking_form,
#             'property_id': property_id,
#             'date_of_viewing': date_of_viewing,
#             'time_of_viewing': time_of_viewing,
#             'f_name': f_name,
#             'l_name': l_name,
#             'client_email': client_email,
#             'client_country': client_country,
#             'client_phone': client_phone,
#             'client_city': client_city,
#             'client_zip': client_zip,
#             'client_message': client_message,
#             'date_submitted': date_submitted,
#             'contact_ok': contact_ok,
#             'prop': prop,
#         }
#         return render(request, 'book/booking-success.html', context)
#     else:
#         return render(request, 'book/booking-success.html')


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


def user_diary(request):
    """ To list all the bookings in the DB """
    prop = Property.objects.all()
    bookings = Booking.objects.all()

    context = {
        'bookings': bookings,
        'prop': prop,
        }
    return render(request, 'book/bookings.html', context)


def parked(request):
    """ View to render the bookings the parked page """
    return render(request, 'book/parked.html')


def update_booking(request, booking_id):
    """ To update the bookings made by each user """
    booking = Booking.objects.get(pk=booking_id)
    booking_form = BookingForm(request.POST or None, instance=booking)

    context = {
        'booking_form': booking_form,
        'booking': booking,
        }
    return render(request, 'book/update-booking.html', context)


def test(request, property_id):
    """ View to test stuff """
    prop = Property.objects.get(pk=property_id)
    # booking = Booking.objects.get(pk=booking_id)
    client = Client.objects.all()

    # context = {
    #     'prop': prop,
    #     'client': client,
    # }

    if request.method == 'POST':
        # client = request.POST.get('client', 'c_id_error!!')
        # prop_id = get_object_or_404(Property.title_no)
        # prop_id = request.get('pk')
        # property_id = Property.objects.get(pk=property_id)
        property_id = request.POST.get('property_id', 'p_id_error!!')
        date_of_viewing = request.POST['date']
        time_of_viewing = request.POST.get('time', 'n/p')
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
        
        # Turn HTML based "on" into a 'TRUE' or 'FALSE' as required by Django
        if contact_ok == 'on':
            contact_ok = True
        else:
            contact_ok = False

        booking_ins = Booking(
            # client=client,
            # property_id=property_id,
            date_of_viewing=date_of_viewing,
            time_of_viewing=time_of_viewing,
            client_message=client_message,
            date_submitted=date_submitted,
            )
        booking_ins.save()
        print('Booking information has been saved')

        booking_id = Booking.objects.get('id')
        print(booking_id)

        client_ins = Client(
            f_name=f_name,
            l_name=l_name,
            client_email=client_email,
            client_phone=client_phone,
            client_city=client_city,
            client_zip=client_zip,
            client_country=client_country,
            contact_ok=contact_ok,
        )
        client_ins.save()
        print('Client information has been saved')

        # Send an email
        send_mail(
            'Message from ' + f_name + l_name + ' at ' + client_email + ', regarding: ' + property_id,
            'Property: '+property_id+', Date and time of proposed viewing: ' +date_of_viewing+' at ' +time_of_viewing+ ', Message:' +client_message,
            client_email,
            ['bookings@reabook.net', 'someone@realestateagentcustomer.com', client_email, ] # to email address
        )

        booking = {
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

            'prop': prop,
            'client': client,
            'booking_id': booking_id,
        }

        # print(form_data)
        # print(request)
        # print(prop_id.content)
        # return render(request, 'book/booking-success.html', booking)
        return render(request, 'book/test.html', booking)
    else:
        return render(request, 'book/test.html')

    # return render(request, 'book/test.html', context)
