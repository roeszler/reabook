""" Import Modules """
from django.contrib import admin

from .models import Property, Category, Sector

admin.site.register(Property)
admin.site.register(Category)
admin.site.register(Sector)
