""" Import Models """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import RegisterUserFrom
from app_bookings.forms import BookingForm


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
                return redirect('user_diary')
        else:
            messages.success(request, 'Aww Nuts! There was an error Logging In. Please try again...')
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
            messages.success(request, ('Registration Successful!'))
            return redirect('user_diary')
        else:
            messages.success(request, 'There was an error with the details on your Registration Form. Please try again...')
            return redirect('register')
    else:
        registration_form = RegisterUserFrom()

    context = {
        'registration_form': registration_form,
    }
    return render(request, 'diary/register.html', context)


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
