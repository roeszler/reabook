""" Import Modules """
from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    """ To customize the django form to a Bookings form """
    # category = forms.CharField(max_length=75)
    class Meta:
        model = Property
        fields = '__all__'
        # fields = (
        #     'category',
        #     'sector',
        #     'title_no',
        #     'name',
        #     'ribbon_feature',
        #     'description',
        #     'sale_price',
        #     'rent_pw',
        #     'rating',
        #     'main_image_url',
        #     'main_image',
        #     'bath_image',
        #     'kitchen_image',
        #     'bedroom_image',
        #     'living_image',
        #     'main_image',
        #     'bedrooms',
        #     'bathrooms',
        #     'carports',
        #     'land_area',
        #     'building_area',
        #     'air_conditioning',
        #     'unit_no',
        #     'house_no',
        #     'level',
        #     'street',
        #     'suburb',
        #     'city',
        #     'state',
        #     'country',
        #     'postcode',
        #     'build_date',
        #     'list_date',
        #     'list_duration',
        #     'date_available',
        #     'owner_fname',
        #     'owner_lname',
        #     'viewings',
        #     'realtor',
        # )
        # widgets = {
        #     'category': forms.ModelMultipleChoiceField(queryset=category, attrs={'class':'form-control col-lg-12', }),
        #     'f_name': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
        #     'l_name': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
        #     'client_username': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
        #     'client_phone': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
        #     'date_of_viewing': forms.DateInput(attrs={'class':'form-control col-lg-12', }),
        #     'time_of_viewing': forms.TimeInput(attrs={'class':'form-control col-lg-12', }),
        #     'client_message': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
        #     'client_password': forms.TextInput(attrs={'class':'form-control col-lg-5', 'placeholder':'password', }),
        # }
        # labels = {
        #     'f_name': 'First Name',
        #     'l_name': 'Last Name',
        #     'client_username': 'Username',
        #     'client_email': 'Email Address',
        #     'client_phone': 'Phone Number',
        #     'date_of_viewing': 'Date of Viewing Appointment',
        #     'time_of_viewing': 'Time of Appointment',
        #     'client_message': 'Messages: ',
        #     'contact_ok': 'Permission to refer for other Properties',
        #     # 'client_password': 'Password',
        # }
