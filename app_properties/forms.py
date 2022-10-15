""" Import Modules """
from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    """ To allow staff / agents to read and update properties in the db """
    # category = forms.CharField(max_length=75)
    class Meta:
        model = Property
        fields = '__all__'

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control col-12', }),
            'sector': forms.Select(attrs={'class': 'form-control col-lg-12', }), # noqa
            'title_no': forms.TextInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'LT-0000',}), # noqa
            'ribbon_feature': forms.TextInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'New Listing',}), # noqa
            'name': forms.TextInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'Friendly Property Name', }), # noqa
            'description': forms.Textarea(attrs={'class': 'form-control col-lg-12', 'placeholder': 'Sights, Sounds, Smells, Social and Sensations.',}), # noqa
            'sale_price': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '1234567', }), # noqa
            'rent_pw': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '1234', }), # noqa
            'rating': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '0.0 / 5',}), # noqa
            'main_image_url': forms.URLInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'https://',}), # noqa
            'main_image': forms.FileInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '448 x 448 pixels',}), # noqa
            'bath_image': forms.FileInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '448 x 448 pixels',}), # noqa
            'kitchen_image': forms.FileInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '448 x 448 pixels',}), # noqa
            'bedroom_image': forms.FileInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '448 x 448 pixels', }), # noqa
            'living_image': forms.FileInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '448 x 448 pixels', }), # noqa
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '3', }), # noqa
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '1', }), # noqa
            'carports': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '1', }), # noqa
            'land_area': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'sqm', }), # noqa
            'building_area': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'sqm', }), # noqa
            'air_conditioning': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '1',}), # noqa
            'unit_no': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '11', }), # noqa
            'house_no': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '22', }), # noqa
            'level': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '1', }), # noqa
            'street': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Burger Way',}), # noqa
            'suburb': forms.TextInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'Tomato Hills',}), # noqa
            'city': forms.TextInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'Pickleton',}), # noqa
            'state': forms.TextInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'Tastyville',}), # noqa
            'country': forms.Select(attrs={'class': 'form-control col-lg-12', 'placeholder': 'Burgeon',}), # noqa
            'postcode': forms.TextInput(attrs={'class': 'form-control col-lg-12', 'placeholder': '123 45',}), # noqa
            'build_date': forms.DateInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'yyyy-mm-dd', }), # noqa
            'list_date': forms.DateInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'yyyy-mm-dd', }), # noqa
            'date_available': forms.DateInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'yyyy-mm-dd', }), # noqa
            'list_duration': forms.NumberInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'days', }), # noqa
            'owner_fname': forms.TextInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'First Name',  }), # noqa
            'owner_lname': forms.TextInput(attrs={'class': 'form-control col-lg-12', 'placeholder': 'Last Name',  }), # noqa
            'realtor': forms.Select(attrs={'class': 'form-control col-lg-12', }), # noqa
        }
