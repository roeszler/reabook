""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_bookings, name='view_bookings'),
]
