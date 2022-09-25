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

        widgets = {
            'category': forms.Select(attrs={'class':'form-control col-12', }),
            'sector': forms.Select(attrs={'class':'form-control col-lg-12', }),
            # 'title_no': forms.CharField(attrs={'class':'form-control col-lg-12', }),
            'title_no': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'ribbon_feature': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'name': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'description': forms.Textarea(attrs={'class':'form-control col-lg-12', }),
            'sale_price': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'rent_pw': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'rating': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'main_image_url': forms.URLInput(attrs={'class':'form-control col-lg-12', }),
            'main_image': forms.FileInput(attrs={'class':'form-control col-lg-12', }),
            'bath_image': forms.FileInput(attrs={'class':'form-control col-lg-12', }),
            'kitchen_image': forms.FileInput(attrs={'class':'form-control col-lg-12', }),
            'bedroom_image': forms.FileInput(attrs={'class':'form-control col-lg-12', }),
            'living_image': forms.FileInput(attrs={'class':'form-control col-lg-12', }),
            'bedrooms': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'bathrooms': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'carports': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'land_area': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'building_area': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'air_conditioning': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'unit_no': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'house_no': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'level': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'street': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'suburb': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'city': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'state': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'country': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'postcode': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'build_date': forms.DateInput(attrs={'class':'form-control col-lg-12', }),
            'list_date': forms.DateInput(attrs={'class':'form-control col-lg-12', }),
            'date_available': forms.DateInput(attrs={'class':'form-control col-lg-12', }),
            'list_duration': forms.NumberInput(attrs={'class':'form-control col-lg-12', }),
            'owner_fname': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'owner_lname': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            'realtor': forms.TextInput(attrs={'class':'form-control col-lg-12', }),
            # 'viewings': forms.CheckboxInput(attrs={'class':'form-control col-lg-12', }),
        #     'client_password': forms.TextInput(attrs={'class':'form-control col-lg-5', 'placeholder':'can't be blank', }),
        }

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
