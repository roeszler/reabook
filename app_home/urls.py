""" Import Modules """
from django.urls import path

# from app_properties.models import Property
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('properties/', Property.name, name='property_name'),
]
