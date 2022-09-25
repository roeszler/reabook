""" Import Models """
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserFrom(UserCreationForm):
    # email = forms.EmailField()
    first_name = forms.CharField(max_length=75)
    last_name = forms.CharField(max_length=75)
    username = forms.CharField(max_length=140)
    # password1 = forms.CharField(max_length=140)
    # password2 = forms.CharField(max_length=140)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )