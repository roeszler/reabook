""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    path('diary/', views.user_diary, name='user_diary'),
    path('diary/<int:booking_id>/', views.update_booking, name='update_booking'),
    path('', views.choose_bookings, name='choose_bookings'),
    path('parked/', views.parked, name='parked'),
    path('detail/<int:property_id>/', views.booking_detail, name='booking_detail'),
    path('choose/<int:property_id>/', views.add_to_diary, name='add_to_diary'),
    path('booked/<int:property_id>/', views.add_booking, name='add-booking'),
]
