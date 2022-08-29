""" Import Modules """
from django.shortcuts import render


def view_properties(request):
    """
    View to render the properties page
    Looks within the current directory app_properties/templates/properties/properties.html
    """
    return render(request, 'properties/properties.html')
