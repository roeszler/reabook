from django.shortcuts import render


def view_my_bookings(request):
    """
    View to render the bookings page
    Looks within the current directory app_bookings/templates/book/book.html
    """
    return render(request, 'book/bookings.html')


def choose_bookings(request):
    """
    View to render the bookings page
    Looks within the current directory app_bookings/templates/book/book.html
    """
    return render(request, 'book/choose-property.html')


def view_bookings_home(request):
    """
    View to render the bookings page
    Looks within the current directory app_bookings/templates/book/book.html
    """
    return render(request, 'book/bookings-base.html')
