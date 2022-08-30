""" Import Modules """
from django.contrib import admin

from .models import Property, Category, Sector

class PropertyAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for properties """
    list_display = (
        'pk',
        'list_date',
        'title_no',
        # 'owner_fname',
        # 'owner_lname',
        # 'unit_no',
        'house_no',
        'street',
        # 'suburb',
        'city',
        # 'country',
        'postcode',
        'sale_price',
        'rent_pw',
        # 'category',
        'main_image',
    )

    ordering = (
        '-pk', 'list_date', 'sale_price', 'rent_pw', 'owner_lname',
        'city', 'postcode', 'title_no', 'category'
    )


class CategoryAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for categories """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name', )


class SectorAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for market sectors """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('-friendly_name', )

admin.site.register(Property, PropertyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sector, SectorAdmin)
