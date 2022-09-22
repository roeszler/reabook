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
    return render(request, 'diary/login.html', {})


def register_user(request):
    """ To render the bookings page with clients upcoming appointments """
    return render(request, 'diary/register.html', {})
