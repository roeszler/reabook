""" Import Modules """
from django import forms
from .models import Client, Booking


class BookingForm(forms.ModelForm):
    """ To customize the django form to a Bookings form """
    class Meta:
        model = Booking
        # fields = '__all__'
        fields = (
            'f_name',
            'l_name',
            'client_username',
            'client_email',
            'client_phone',
            'date_of_viewing',
            'time_of_viewing',
            'client_message',
            'contact_ok',
        )

        labels = {
            'f_name': 'First Name ',
            'l_name': 'Last Name',
            'client_username': 'Username',
            'client_email': 'Email Address',
            'client_phone': 'Phone Number',
            'date_of_viewing': 'Date of Viewing Appointment',
            'time_of_viewing': 'Time of Appointment',
            'client_message': 'Messages: ',
            'contact_ok': 'Permission to refer for other Properties',
            # 'client_password': 'Password',
        }
        widgets = {
            'client_email': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'f_name': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'l_name': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'client_username': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'client_phone': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'date_of_viewing': forms.DateInput(attrs={'class':'form-control col-lg-12', }),
            'time_of_viewing': forms.TimeInput(attrs={'class':'form-control col-lg-12', }),
            'client_message': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'client_password': forms.TextInput(attrs={'class':'form-control col-lg-5', 'placeholder':'password', }),
        }


class ClientForm(forms.ModelForm):
    """ To customize the django form to a Bookings form """
    class Meta:
        model = Client
        # fields = '__all__'
        fields = (
            'f_name',
            'l_name',
            'client_email',
            'client_phone',
            'contact_ok',
        )


class LoginForm(forms.ModelForm):
    """ To customize the django form to a Bookings form """

    class Meta:
        """ Indicate associations and editable user input fields """
        model = Client
        fields = (
            # 'f_name', 'l_name', 'client_username',
            'client_email',
            # 'client_phone',
            # 'client_city', 'client_state', 'client_zip',
            # 'client_country', 'contact_ok',
        )

        labels = {
            'client_email': 'Username or Email',
            # 'client_password': 'Password',
        }

        widgets = {
            'client_email': forms.TextInput(attrs={'class':'form-control ml-5 mr-1 col-lg-5', 'placeholder':'Username or Email', }),
            'client_password': forms.TextInput(attrs={'class':'form-control mr-5 ml-1 col-lg-5', 'placeholder':'password', }),
        }
