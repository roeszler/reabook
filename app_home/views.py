""" Import Modules """
from django.shortcuts import render

from app_properties.models import Property, Category, Sector


def index(request):
    """
    View to return the index.html page
    """
    properties = Property.objects.all()
    categories = Category.objects.all()
    sectors = Sector.objects.all()

    context = {
        'properties': properties,
        'categories': categories,
        'sectors': sectors,
    }
    return render(request, 'home/index.html', context)


# def all_properties(request):
#     """
#     View to access all properties in the index.html page
#     """
#     properties = Property.objects.all()

#     context = {
#         'properties': properties,
#     }
#     return render(request, '/index.html', context)
