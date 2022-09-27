""" Import Modules """
import pytz
from django.db import models
from django.contrib.auth.models import User


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
        # return f"{self.id}"

    def get_friendly_name(self):
        """ Takes in the category model to return friendly_name """
        return self.friendly_name


class Sector(models.Model):
    """ To contain the data from the categories.json fixtures file  """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Takes in the sector model to return db name """
        return self.name
        # return f"{self.id}"

    def get_friendly_name(self):
        """ Takes in the sector model to return friendly_name """
        return self.friendly_name


class Property(models.Model):
    """ To contain the data from the properties.json fixtures file  """
    realtor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False, default=User)
    title_no = models.CharField(max_length=254)
    ribbon_feature = models.CharField(max_length=20, default="New Listing")
    name = models.CharField(max_length=30)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    sector = models.ForeignKey(
        'Sector', null=True, blank=True, on_delete=models.SET_NULL
        )
    sale_price = models.IntegerField(null=False, blank=True, default=0)
    rent_pw = models.IntegerField(null=False, blank=True, default=0)
    date_available = models.DateField(null=True, blank=True, auto_now_add=True)
    bedrooms = models.IntegerField(null=False, blank=False)
    bathrooms = models.IntegerField(null=False, blank=False)
    carports = models.IntegerField(null=False, blank=False)
    air_conditioning = models.IntegerField(null=False, blank=False)
    rating = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
        )
    description = models.TextField()
    main_image_url = models.URLField(max_length=1024, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)
    bedroom_image = models.ImageField(null=True, blank=True)
    bath_image = models.ImageField(null=True, blank=True)
    kitchen_image = models.ImageField(null=True, blank=True)
    living_image = models.ImageField(null=True, blank=True)

    unit_no = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    house_no = models.IntegerField(null=True, blank=False, default="No.")
    street = models.CharField(max_length=70, default='')
    suburb = models.CharField(max_length=70, default='')
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=2, choices=pytz.country_names.items(), null=True, blank=True)
    land_area = models.IntegerField(null=True, blank=True)
    building_area = models.IntegerField(null=True, blank=True)
    build_date = models.DateField(null=True, blank=True)
    list_date = models.DateField(auto_now_add=True)
    list_duration = models.IntegerField(null=False, blank=False, default=30)
    owner_fname = models.CharField(max_length=254, null=True, blank=False)
    owner_lname = models.CharField(max_length=254, null=True, blank=False)
    viewings = models.BooleanField(default=False)
    available = models.BooleanField(default=False)

    class Meta:
        """ to adjust the verbose name or the plural form from defaults """
        verbose_name_plural = 'Properties'
        get_latest_by = 'list_date'

    def __str__(self):
        """ Takes in product display model and returns name """
        # return f"{self.id} = {self.house_no} {self.street}, {self.suburb}, {self.city}"
        # return f"ID.{self.id} ({self.house_no} {self.street}, {self.suburb}, {self.city})"
        return f"{self.id}"
    
    # def __int__(self):
    #     """ Takes in product display model and returns name """
    #     return self.title_no
