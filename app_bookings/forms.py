""" Import Modules """
from django import forms
  
# iterable
GEEKS_CHOICES =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

# creating a form 
class GeeksForm(forms.Form):
    """ Form to allow radio selection of session in models.Slot """
    geeks_field = forms.ChoiceField(choices=GEEKS_CHOICES, widget=forms.RadioSelect())
