""" Import Modules """
from django import forms
from .models import Booking, Client


class BookingForm(forms.ModelForm):
    """ To customize the django form to a Bookings form """

    class Meta:
        """ Indicate associations and editable user input fields """
        model = Booking
        fields = (
            'date_of_viewing',
            'time_of_viewing', 'client_message',
        )


class ClientForm(forms.ModelForm):
    """ To customize the django form to a Bookings form """

    class Meta:
        """ Indicate associations and editable user input fields """
        model = Client
        fields = (
            'f_name', 'l_name', 'client_username',
            'client_email', 'client_phone',
            'client_city', 'client_state', 'client_zip',
            'client_country', 'contact_ok',
        )


# # creating a form 
# class GeeksForm(forms.Form):
#     """ Form to allow radio selection of session in models.Slot """
#     geeks_field = forms.ChoiceField(choices=GEEKS_CHOICES, widget=forms.RadioSelect())
