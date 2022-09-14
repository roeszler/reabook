""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.view_bookings_home, name='bookings_home'),
    path('', views.view_my_bookings, name='my_bookings'),
    # path('booked/', views.view_my_bookings, name='my_bookings'),
    path('choose/', views.choose_bookings, name='choose_bookings'),
    path('login/', views.view_bookings_login, name='bookings_login'),

    path('details/', views.view_booking_detail, name='request_details'),
    
    path('time/', views.view_booking_select_time, name='select_time'),
    path('time/<int:property_id>/', views.view_booking_detail, name='booking_detail'),
    path('success/', views.view_booking_success, name='booking_success'),
    path('choose/<int:property_id>/', views.add_to_diary, name='add_to_diary')
]
