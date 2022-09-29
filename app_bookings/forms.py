""" Import Modules """
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """ To customize the django form to a Bookings form """
    # category = forms.CharField(max_length=75)

    class Meta:
        model = Booking
        # fields = '__all__'
        fields = (
            'contact_ok', 'viewing_active', 'property_id',
            'date_of_viewing', 'client_username', 'time_of_viewing',
            'client_email', 'f_name', 'l_name', 'client_phone',
            'client_city', 'client_zip', 'client_country', 'client_message',
        )
        widgets = {
            'client_email': forms.EmailInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'your@email.com', }),
            'f_name': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'First Name', }),
            'l_name': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Last Name', }),
            'client_username': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'ReaBookBob1', }),
            'client_phone': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': '555 123-456-789', }),
            'client_city': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Paradise City', }),
            'client_zip': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': '123 45', }),
            'client_country': forms.Select(attrs={'class':'form-control col-lg-12', 'placeholder': 'Tasteville', }),
            'client_message': forms.Textarea(attrs={'class':'form-control col-lg-12', 'rows': '3', 'max-rows': '6', }),
            # 'client_password': forms.PasswordInput(attrs={'class':'form-control col-lg-5', 'placeholder':'password', }),
        }
