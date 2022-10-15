""" Import Modules """
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Property, Category, Sector
from .forms import PropertyForm

from app_bookings.models import Booking


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
                properties = properties.annotate(lower_name_annotation=Lower('name')) # noqa

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

            # Q to generate a non-sensitive query by name OR description
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ribbon_feature__icontains=query) | Q(sale_price__icontains=query) | Q(rent_pw__icontains=query) | Q(suburb__icontains=query) | Q(street__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query) | Q(country__icontains=query) | Q(postcode__icontains=query)  # noqa
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


@login_required
def manage_properties(request, user_id):
    """ View allowing Staff / Agents to admin the properties they manage """
    properties = Property.objects.all()  # noqa
    users_properties = properties.filter(realtor=user_id)
    user = get_object_or_404(User, pk=user_id)

    if user.is_authenticated:
        users_bookings = Booking.objects.filter(user=user) # noqa
        bookings_count = users_bookings.count()
        request.session['bookings_count'] = users_bookings.count()
    else:
        bookings_count = 0

    context = {
        'user': user,
        'users_properties': users_properties,
        'bookings_count': bookings_count,
    }
    return render(request, 'properties/manage-properties.html', context)


@login_required
def edit_property(request, property_id):
    """ A view to allow staff to edit individual property details """
    prop = Property.objects.get(pk=property_id)  # noqa
    # prop = get_object_or_404(Property, pk=property_id)
    property_form = PropertyForm(instance=prop)

    if prop.realtor == request.user:
        if request.method == 'POST':
            property_form = PropertyForm(request.POST, request.FILES, instance=prop) # noqa
            if property_form.is_valid():
                prop_f = property_form.save(False)
                prop_f.user = request.user
                prop_f.save()
                print('Edit to property information has been saved')
                messages.success(request, f'Property id.{property_id}\
                    has been successfully updated!')
                return redirect(f'/properties/{prop.id}/')
    else:
        print('You do not have permission to edit this property')
        messages.success(request, f'You do not have permission to\
            edit this property, id.{property_id}.')

    context = {
        'prop': prop,
        'property_form': property_form,
    }
    return render(request, 'properties/edit-properties.html', context)


@login_required
def add_property(request, realtor_id):
    """ A view to allow staff to add a new property """
    prop = User.objects.get(id=realtor_id)
    property_form = PropertyForm(instance=prop)
    user = request.user

    if request.method == 'POST':
        property_form = PropertyForm(request.POST, request.FILES, instance=prop) # noqa
        if property_form.is_valid():
            prop_f = property_form.save(commit=False)
            prop_f.user = user
            prop_f.save()
            print('New Property information has been listed')
            # return redirect(f'/properties/manage/{user.id}/')
            return redirect(f'/properties/{prop_f.id}/')

    context = {
        'prop': prop,
        'property_form': property_form,
    }

    return render(request, 'properties/add-properties.html', context)


@login_required
def delete_property(request, property_id):
    """ A view to authorize and manage the delete property events """
    prop = get_object_or_404(Property, pk=property_id)
    user = request.user

    if prop.realtor != request.user:
        messages.error(request, 'Sorry, only authorized agents can do that.')
        return redirect(reverse('properties'))
    else:
        # prop.delete()
        print(f'Property id.{property_id} Deleted')
        messages.success(request, f'Property id.{property_id} deleted!')
        return redirect(f'/properties/manage/{user.id}/')
