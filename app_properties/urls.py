""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_properties, name='view_properties'),
]
