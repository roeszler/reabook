""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_properties, name='properties'),
    path('<int:property_id>/', views.property_detail, name='property_detail'),
]
