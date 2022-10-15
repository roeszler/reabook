""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    path('diary/<int:user_id>/', views.my_diary, name='user-diary'),
    path('diary/edit/<int:booking_id>/', views.update_booking, name='update-booking'), # noqa
    path('diary/delete/<int:booking_id>/', views.delete_booking, name='delete-booking'), # noqa
    path('', views.choose_bookings, name='choose_bookings'),
    path('parked/', views.parked, name='parked'),
    path('detail/<int:property_id>/', views.booking_detail, name='booking-detail'),  # noqa
    path('choose/<int:property_id>/', views.add_to_diary, name='add_to_diary'),
    path('booked/<int:property_id>/', views.add_booking, name='add-booking'),
]
