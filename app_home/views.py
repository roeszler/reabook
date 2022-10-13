""" Import Modules """
from django.shortcuts import render

from app_properties.models import Property
from app_bookings.models import Booking


def index(request):
    """ View to return the index.html page """
    properties = Property.objects.all() # noqa
    props_latest = properties.order_by('list_date')
    props_for_rent = properties.filter(category__name="for_rent")
    props_for_sale = properties.filter(category__name="for_sale")
    props_for_lease = properties.filter(category__name="for_lease")

    user = request.user
    users_bookings = Booking.objects.filter(user=user) # noqa
    bookings_count = users_bookings.count()
    request.session['bookings_count'] = users_bookings.count()

    context = {
        'properties': properties,
        'props_latest': props_latest,
        'props_for_rent': props_for_rent,
        'props_for_sale': props_for_sale,
        'props_for_lease': props_for_lease,
        'bookings_count': bookings_count,
    }
    return render(request, 'home/index.html', context)
