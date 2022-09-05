""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_bookings_home, name='bookings_home'),
    path('choose/', views.view_bookings_stage_1, name='bookings_stage_1'),
]
