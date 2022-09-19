""" Import Modules """
from django.contrib import admin

from .models import Property, Category, Sector


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for properties """
    list_display = (
        'pk',
        'title_no',
        'list_date',
        'house_no',
        'street',
        'city',
        'postcode',
        'city',
        'country',
        'category',
        'sector',
        'sale_price',
        'rent_pw',
        'realtor',
        # 'main_image',
    )

    ordering = (
        'pk', 'title_no', 'list_date', 'sale_price', 'rent_pw', 'owner_lname',
        'city', 'postcode', 'country', 'category', 'sector', 'realtor',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section for categories """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name', )


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    """ To edit the fields shown on the django admin section 'sectors' """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('-friendly_name', )


# admin.site.register(Property, PropertyAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Sector, SectorAdmin)
