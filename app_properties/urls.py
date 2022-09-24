""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_properties, name='properties'),
    path('<int:property_id>/', views.property_detail, name='property-detail'),
    # path('add/', views.add_property, name='edit-property'),
    path('edit/<int:property_id>/', views.edit_property, name='edit-property'),
]
