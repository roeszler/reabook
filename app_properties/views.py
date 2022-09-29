""" Import Modules """
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User

from .models import Property, Category, Sector
from .forms import PropertyForm


def all_properties(request):
    """ Renders all properties, including search queries and sorting """
    properties = Property.objects.all()
    query = None
    categories = None
    sectors = None
    sort = None
    direction = None

    # search function
    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name_annotation'
                properties = properties.annotate(lower_name_annotation=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'descending':
                    sortkey = f'-{sortkey}'
            
            properties = properties.order_by(sortkey)

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
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('properties'))

            # Using Q to generate a non-sensitive search query by name OR description
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ribbon_feature__icontains=query) | Q(sale_price__icontains=query) | Q(rent_pw__icontains=query) | Q(suburb__icontains=query) | Q(street__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query) | Q(country__icontains=query) | Q(postcode__icontains=query)
            properties = properties.filter(queries)

    # To return the current sorting methodology to the template
    current_sorting = f'{sort}_{direction}'

    context = {
        'properties': properties,
        'search_term': query,
        'current_categories': categories,
        'current_sectors': sectors,
        'current_sorting': current_sorting,
    }
    return render(request, 'properties/properties.html', context)


def property_detail(request, property_id):
    """ A view to show individual property details """
    prop = get_object_or_404(Property, pk=property_id)
    context = {
        'prop': prop,
    }
    return render(request, 'properties/prop-detail.html', context)


def manage_properties(request, user_id):
    """ View allowing Staff / Agents to admin the properties they manage """
    properties = Property.objects.all()
    users_properties = properties.filter(realtor=user_id)
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user,
        'users_properties': users_properties,
    }
    return render(request, 'properties/manage-properties.html', context)


def edit_property(request, property_id):
    """ A view to allow staff to edit individual property details """
    prop = Property.objects.get(pk=property_id)
    property_form = PropertyForm(instance=prop)

    if request.method == 'POST':
        property_form = PropertyForm(request.POST, request.FILES, instance=prop)
        if property_form.is_valid():
            prop_f = property_form.save(False)
            prop_f.user = request.user
            prop_f.save()
            print('Edit to property information has been saved')

    context = {
        'prop': prop,
        'property_form': property_form,
    }
    return render(request, 'properties/edit-properties.html', context)


def add_property(request, realtor_id):
    """ A view to allow staff to add a new property """
    prop = User.objects.get(id=realtor_id)
    property_form = PropertyForm(instance=prop)

    if request.method == 'POST':
        property_form = PropertyForm(request.POST, request.FILES)
        if property_form.is_valid():
            prop_f = property_form.save(commit=False)
            prop_f.user = request.user
            prop_f.save()
            print('New Property information has been saved')

    context = {
        'prop': prop,
        'property_form': property_form,
    }

    return render(request, 'properties/add-properties.html', context)


def delete_property(request, property_id):
    """ A view to authorize and manage the delete property events """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized agents can do that.')
        return redirect(reverse('properties'))

    prop = get_object_or_404(Property, pk=property_id)
    user = request.user
    prop.delete()
    print(f'Property id.{property_id} Deleted')
    messages.success(request, f'Property id.{property_id} deleted!')
    return redirect(f'/properties/manage/{user.id}/')
