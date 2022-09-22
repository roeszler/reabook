""" Import Modules """
from django.urls import path
from . import views


urlpatterns = [
    path('account/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
]
