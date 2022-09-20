""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    path('diary/', views.client_diary, name='client_diary'),
    path('', views.choose_bookings, name='choose_bookings'),
    path('login/', views.login, name='bookings_login'),
    path('detail/<int:property_id>/', views.booking_detail, name='booking_detail'),
    path('success/', views.booking_success, name='booking_success'),
    path('choose/<int:property_id>/', views.add_to_diary, name='add_to_diary'),
    path('test/', views.test, name='test'),
]
