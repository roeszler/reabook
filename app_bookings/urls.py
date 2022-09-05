""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_bookings_home, name='bookings_home'),
    path('booked/', views.view_my_bookings, name='my_bookings'),
    path('choose/', views.choose_bookings, name='choose_bookings'),
]
