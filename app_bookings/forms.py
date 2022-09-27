""" Import Modules """
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """ To customize the django form to a Bookings form """
    # category = forms.CharField(max_length=75)

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'client_email': forms.EmailInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'your@email.com', }),
            'f_name': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'First Name', }),
            'l_name': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Last Name', }),
            'client_username': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'ReaBookBob', }),
            'client_phone': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': '555 123-456-789', }),
            'client_city': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Paradise City', }),
            'client_zip': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': '123 45', }),
            'client_country': forms.Select(attrs={'class':'form-control col-lg-12', 'placeholder': 'Tasteville', }),
            'date_of_viewing': forms.DateInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'YYYY-MM-DD', }),
            'time_of_viewing': forms.TimeInput(attrs={'class':'form-control col-lg-12','placeholder': 'YYYY-MM-DD', }),
            'client_message': forms.Textarea(attrs={'class':'form-control col-lg-12', 'rows': '3', 'max-rows': '6', }),
            'client_password': forms.PasswordInput(attrs={'class':'form-control col-lg-5', 'placeholder':'password', }),
        }


# class ClientForm(forms.ModelForm):
#     """ To customize the django form to a Bookings form """
#     class Meta:
#         model = Client
#         # fields = '__all__'
#         fields = (
#             'f_name',
#             'l_name',
#             'client_email',
#             'client_phone',
#             'contact_ok',
#         )


# class LoginForm(forms.ModelForm):
#     """ To customize the django form to a Bookings form """

#     class Meta:
#         """ Indicate associations and editable user input fields """
#         model = Client
#         fields = (
#             # 'f_name', 'l_name', 'client_username',
#             'client_email',
#             # 'client_phone',
#             # 'client_city', 'client_state', 'client_zip',
#             # 'client_country', 'contact_ok',
#         )

#         labels = {
#             'client_email': 'Username or Email',
#             # 'client_password': 'Password',
#         }

#         widgets = {
#             'client_email': forms.TextInput(attrs={'class':'form-control ml-5 mr-1 col-lg-5', 'placeholder':'Username or Email', }),
#             'client_password': forms.TextInput(attrs={'class':'form-control mr-5 ml-1 col-lg-5', 'placeholder':'password', }),
#         }
