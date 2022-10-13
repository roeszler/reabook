""" Import Modules """
from django.shortcuts import render
from django.contrib.auth.models import User

from app_bookings.models import Booking


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def bookings_count(request):
    """ Return the total number of bookings for the logged in user """
    user = request.user
    users_bookings = Booking.objects.filter(user=user) # noqa
    no_bookings = users_bookings.count()

    context = {
        'no_bookings': no_bookings,
    }
    return render(request, 'base.html', context)
