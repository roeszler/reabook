""" Import Modules """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_properties, name='properties'),
    path('<int:property_id>/', views.property_detail, name='property-detail'),
    path('add/<int:realtor_id>/', views.add_property, name='add-property'),
    path('edit/<int:property_id>/', views.edit_property, name='edit-property'),
    path('manage/<int:user_id>/', views.manage_properties, name='manage-properties'),
    path('delete/<int:property_id>/', views.delete_property, name='delete-property'),
    # path('manage/<int:user_id>/', views.delete_property, name='delete-property'),
]
