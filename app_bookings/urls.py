""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.view_bookings_home, name='bookings_home'),
    path('diary/', views.client_bookings, name='client_bookings'),
    # path('booked/', views.view_my_bookings, name='my_bookings'),
    path('', views.choose_bookings, name='choose_bookings'),
    path('login/', views.view_bookings_login, name='bookings_login'),

    # path('details/', views.view_booking_detail, name='request_details'),

    # path('time/', views.view_booking_select_time, name='select_time'),
    path('detail/<int:property_id>/', views.booking_detail, name='booking_detail'),
    path('success/', views.booking_success, name='booking_success'),
    path('choose/<int:property_id>/', views.add_to_diary, name='add_to_diary')
]
