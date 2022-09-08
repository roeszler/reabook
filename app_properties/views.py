""" Import Modules """
from django.shortcuts import render, get_object_or_404

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


def property_detail(request, property_id):
    """ A view to show individual property details """
    prop = get_object_or_404(Property, pk=property_id)
    context = {
        'prop': prop,
    }
    return render(request, 'properties/prop-detail.html', context)
