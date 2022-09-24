""" Import Models """
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserFrom(UserCreationForm):
    # email = forms.EmailField()
    # first_name = forms.CharField(max_length=75)
    # last_name = forms.CharField(max_length=75)
    # username = forms.CharField(max_length=140)
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
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Repeat Password'
        }
        widgets = {
            # 'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.' }),
            'username': forms.TextInput(attrs={'class':'form-control', }),
            'first_name': forms.TextInput(attrs={'class':'form-control', }),
            'last_name': forms.TextInput(attrs={'class':'form-control', }),
            'email': forms.EmailInput(attrs={'class':'form-control col-lg-12', }),
            'password1': forms.TextInput(attrs={'class':'form-control', }),
            # 'password1': forms.PasswordInput(attrs={'class':'form-control', }),
            'password2': forms.PasswordInput(attrs={'class':'form-control', }),
        }
