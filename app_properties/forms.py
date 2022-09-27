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
            'category': forms.Select(attrs={'class':'form-control col-12', }),
            'sector': forms.Select(attrs={'class':'form-control col-lg-12', }),
            'title_no': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'LT-0000',}),
            'ribbon_feature': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'New Listing',}),
            'name': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Friendly Property Name', }),
            'description': forms.Textarea(attrs={'class':'form-control col-lg-12', 'placeholder': 'Sights, Sounds, Smells, Social and Sensations.',}),
            'sale_price': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': '1234567', }),
            'rent_pw': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': '1234', }),
            'rating': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': '0.0 / 5',}),
            'main_image_url': forms.URLInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'https://',}),
            'main_image': forms.FileInput(attrs={'class':'form-control col-lg-12', 'placeholder': '448 x 448 pixels',}),
            'bath_image': forms.FileInput(attrs={'class':'form-control col-lg-12', 'placeholder': '448 x 448 pixels',}),
            'kitchen_image': forms.FileInput(attrs={'class':'form-control col-lg-12', 'placeholder': '448 x 448 pixels',}),
            'bedroom_image': forms.FileInput(attrs={'class':'form-control col-lg-12', 'placeholder': '448 x 448 pixels', }),
            'living_image': forms.FileInput(attrs={'class':'form-control col-lg-12', 'placeholder': '448 x 448 pixels', }),
            'bedrooms': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': '3', }),
            'bathrooms': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': '1', }),
            'carports': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': '1', }),
            'land_area': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'sqm', }),
            'building_area': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'sqm', }),
            'air_conditioning': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': '1',}),
            'unit_no': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': '11', }),
            'house_no': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': '22', }),
            'level': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': '1', }),
            'street': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Burger Way',}),
            'suburb': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Tomato Hills',}),
            'city': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Pickleton',}),
            'state': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Tastyville',}),
            'country': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Burgeon',}),
            'postcode': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': '123 45',}),
            'build_date': forms.DateInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'yyyy-mm-dd', }),
            'list_date': forms.DateInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'yyyy-mm-dd', }),
            'date_available': forms.DateInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'yyyy-mm-dd', }),
            'list_duration': forms.NumberInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'days', }),
            'owner_fname': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'First Name',  }),
            'owner_lname': forms.TextInput(attrs={'class':'form-control col-lg-12', 'placeholder': 'Last Name',  }),
            'realtor': forms.Select(attrs={'class':'form-control col-lg-12', }),
        }
