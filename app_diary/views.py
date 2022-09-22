""" Import Models """
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterUserFrom


def login_user(request):
    """ To log users in via the web interface """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('client_diary')
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
            return redirect('client_diary')
        else:
            messages.success(request, 'There was an error with the details on your Registration Form. Please try again...')
            return redirect('register')
    else:
        registration_form = RegisterUserFrom()

    context = {
        'registration_form': registration_form,
    }
    return render(request, 'diary/register.html', context)
