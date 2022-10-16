""" Import Models """
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserFrom(UserCreationForm):
    """ Form to manage the new client registration data """
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'pass form-control col-12',
            'type': 'password',
            'align': 'left',
            'placeholder': 'password',
            }),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            'class': 'pass form-control col-12',
            'type': 'password',
            'align': 'left',
            'placeholder': 'repeat password',
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
        )

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control my-0 col-12', 'placeholder': 'ReaBookBob1', }), # noqa
            'email': forms.EmailInput(attrs={'class': 'form-control col-12', 'placeholder': 'your@email.com', }), # noqa
            'first_name': forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': 'First Name', }), # noqa
            'last_name': forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': 'Last Name', }), # noqa
        }
    
    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email
