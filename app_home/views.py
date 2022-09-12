""" Import Modules """
from django.shortcuts import render

from app_properties.models import Property, Category


def index(request):
    """
    View to return the index.html page
    """
    properties = Property.objects.all()
    # categories = Category.objects.all()
    # sectors = Sector.objects.all()
    
    # order_by = Property.objects.all().order_by('list_date')
    props_latest = properties.order_by('list_date')
    props_for_rent = properties.filter(category__name="for_rent")
    props_for_sale = properties.filter(category__name="for_sale")
    props_for_lease = properties.filter(category__name="for_lease")

    context = {
        'properties': properties,
        # 'categories': categories,
        # 'sectors': sectors,
        # 'order_by': order_by,
        'props_latest': props_latest,
        'props_for_rent': props_for_rent,
        'props_for_sale': props_for_sale,
        'props_for_lease': props_for_lease,
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
