""" Import Modules """
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ To contain a one to one relationship with the Django user model """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
