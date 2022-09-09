""" Import Modules """
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Property, Category, Sector


def all_properties(request):
    """
    View to render all properties page that includes search queries and sorting
    """
    properties = Property.objects.all()
    query = None
    categories = None
    sectors = None

    # search function
    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            properties = properties.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sector' in request.GET:
            sectors = request.GET['sector'].split(',')
            properties = properties.filter(sector__name__in=sectors)
            sectors = Sector.objects.filter(name__in=sectors)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('properties'))

            # Using Q to generate a non-sensitive search query
            # by name OR description
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ribbon_feature__icontains=query) | Q(sale_price__icontains=query) | Q(rent_pw__icontains=query) | Q(suburb__icontains=query) | Q(street__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query) | Q(country__icontains=query) | Q(postcode__icontains=query)
            properties = properties.filter(queries)

    context = {
        'properties': properties,
        'search_term': query,
        'current_categories': categories,
        'current_sectors': sectors,
    }
    return render(request, 'properties/properties.html', context)


def property_detail(request, property_id):
    """ A view to show individual property details """
    prop = get_object_or_404(Property, pk=property_id)
    context = {
        'prop': prop,
    }
    return render(request, 'properties/prop-detail.html', context)
