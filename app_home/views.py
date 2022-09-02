""" Import Modules """
from django.shortcuts import render

# from .models import ViewPropertyCategories


def index(request):
    """
    View to return the index.html page
    """
    return render(request, 'home/index.html')


# def all_properties(request):
#     """ A view to show all properties, including sorting and search queries """
#     properties = ViewPropertyCategories.objects.all()

#     context = {
#         'properties': properties,
#     }
#     return render(request, 'home/index.html', context)
