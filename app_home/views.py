""" Import Modules """
from django.shortcuts import render

# from .models import ViewPropertyCategories


def index(request):
    """
    View to return the index.html page
    """
    return render(request, 'home/index.html')

