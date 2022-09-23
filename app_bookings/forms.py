""" Import Modules """
from django import forms
from .models import Client, Booking


class BookingForm(forms.ModelForm):
    """ To customize the django form to a Bookings form """
    class Meta:
        model = Booking
        # fields = '__all__'
        fields = (
            'date_of_viewing',
            'time_of_viewing',
            'client_message',
        )


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
