""" Import Models """
# from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# from django.db.models import Q
# from django.core.mail import send_mail
# from django.http import HttpResponseRedirect

# from app_properties.models import Property
# from .models import Booking, Client
# from .forms import LoginForm


def login_user(request):
    """ To render the bookings page with clients upcoming appointments """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('client_diary')
        else:
            messages.success(request, 'Aww Nuts! There was an error Logging you in. Please try again...')
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'diary/login.html', {})


def register_user(request):
    """ To render the bookings page with clients upcoming appointments """
    return render(request, 'diary/register.html', {})
