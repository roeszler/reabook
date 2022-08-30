""" Import Modules """
from django.contrib import admin

from .models import Property, Category, Sector

class PropertyAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for properties """
    list_display = (
        'title_no',
        'sku',
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for categories """


class SectorAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for market sectors """


admin.site.register(Property)
admin.site.register(Category)
admin.site.register(Sector)
