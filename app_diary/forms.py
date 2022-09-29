""" Import Models """
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from app_bookings.models import Booking


class RegisterUserFrom(UserCreationForm):
    # client_phone = forms.IntegerField()
    # password1 = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class':'pass form-control col-12',
            'type':'password',
            'align':'left',
            'placeholder':'password',
            }),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            'class':'pass form-control col-12',
            'type':'password',
            'align':'left',
            'placeholder':'repeat password',
            }),
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            # 'client_phone',
        )

        labels = {
            'username': '',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control my-0 col-12', 'placeholder': 'ReaBookBob1', 'placeholder': 'ReaBookBob1', }),
            'email': forms.EmailInput(attrs={'class':'form-control col-12', 'placeholder': 'your@email.com', }),
            'first_name': forms.TextInput(attrs={'class':'form-control col-12', 'placeholder': 'First Name', }),
            'last_name': forms.TextInput(attrs={'class':'form-control col-12', 'placeholder': 'Last Name', }),
        }
