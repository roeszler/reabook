""" Import Modules """
from django.shortcuts import render

from .models import Property


def all_properties(request):
    """
    View to render all properties page that includes search queries and sorting
    """

    properties = Property.objects.all()

    context = {
        'properties': properties,
    }

    return render(request, 'properties/properties.html', context)
