""" Import Modules """
from django.db import models


class Category(models.Model):
    """ To contain the data from the categories.json fixtures file  """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Categories'

    def __str__(self):
        """ Takes in the category model to return db name """
        return self.name

    def get_friendly_name(self):
        """ Takes in the category model to return friendly_name """
        return self.friendly_name


class Sector(models.Model):
    """ To contain the data from the categories.json fixtures file  """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Takes in the category model to return db name """
        return self.name

    def get_friendly_name(self):
        """ Takes in the category model to return friendly_name """
        return self.friendly_name


class Property(models.Model):
    """ To contain the data from the properties.json fixtures file  """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    sector = models.ForeignKey(
        'Sector', null=True, blank=True, on_delete=models.SET_NULL
        )
    title_no = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=30)
    ribbon_feature = models.CharField(max_length=20, default="New Listing")
    description = models.TextField()
    sale_price = models.IntegerField(null=False, blank=False, default=0)
    rent_pw = models.IntegerField(null=False, blank=False, default=0)
    rating = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
        )
    main_image_url = models.URLField(max_length=1024, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)
    bath_image = models.ImageField(null=True, blank=True)
    kitchen_image = models.ImageField(null=True, blank=True)
    bedroom_image = models.ImageField(null=True, blank=True)
    living_image = models.ImageField(null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)
    bedrooms = models.IntegerField(null=False, blank=False)
    bathrooms = models.IntegerField(null=False, blank=False)
    carports = models.IntegerField(null=False, blank=False)
    land_area = models.IntegerField(null=True, blank=True)
    building_area = models.IntegerField(null=True, blank=True)
    air_conditioning = models.IntegerField(null=False, blank=False)
    unit_no = models.IntegerField(null=True, blank=True)
    house_no = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=40, null=True, blank=True)
    suburb = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=10)
    build_date = models.DateField(null=True, blank=True)
    list_date = models.DateField()
    list_duration = models.IntegerField(null=False, blank=False, default=30)
    date_available = models.DateField(null=True, blank=True)
    owner_fname = models.CharField(max_length=254, null=True, blank=False)
    owner_lname = models.CharField(max_length=254, null=True, blank=False)

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Properties'

    def __str__(self):
        """ Takes in product display model and returns name """
        return self.name
