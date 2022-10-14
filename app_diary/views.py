""" Import Models """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from app_bookings.forms import BookingForm
from .forms import RegisterUserFrom


def login_user(request):
    """ To log users in via the web interface """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser or user.is_staff:
                return redirect(f'/properties/manage/{user.id}/')
            else:
                return redirect(f'/book/diary/{user.id}/')
        else:
            messages.success(request, 'Sorry! There was an error\n\
                Logging in. Please try again...')
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'diary/login.html', {})


def logout_user(request):
    """ To log users out via the web interface """
    logout(request)
    messages.success(request, 'You have been successfully Logged Out.')
    return redirect('home')


def register_user(request):
    """ To allow new users to register via the web interface """
    if request.method == 'POST':
        registration_form = RegisterUserFrom(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data['username']
            password = registration_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, (f'Registration Successful! A new user\
                 has been created \n User id.{user.id} with conformation sent to\
                     {user.email}.\n Please log in again with the details\
                         emailed to you'))
            send_mail(
                'New Registration at ReaBook.net',
                f'Welcome to ReaBook.net {user.first_name}\n\
                    A site to help coordinate property searching.\n\
                    Your registration details are as follows:\n\
                    Username: {user.username}\n\
                    Email: {user.email}\n\
                    Password: {password}\n\
                    New user id. {user.id}\n',
                'reabook@example.com',
                ['registrations@reabook.net', user.email, ],
                fail_silently=False,
            )
            return redirect('choose_bookings')
        else:
            messages.success(request, f'There was an error with the details on\
                 your Registration Form.\n {registration_form.errors}\n\
                    Please try again...')
            print(registration_form.errors)
            return redirect('register')
    else:
        registration_form = RegisterUserFrom()

    context = {
        'registration_form': registration_form,
    }
    return render(request, 'diary/register.html', context)


@login_required
def my_profile(request, user_id):
    """ View to render the profile edit page """
    user = get_object_or_404(User, pk=user_id)
    user_form = RegisterUserFrom(instance=user)
    booking_form = BookingForm(instance=user)

    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            booking_form.save()

        print('Your Profile has been Successfully Updated')
        messages.success(request, 'Your Profile has been Successfully Updated!')

    context = {
        'user': user,
        'user_form': user_form,
        'booking_form': booking_form,
    }
    return render(request, 'diary/profile.html', context)
