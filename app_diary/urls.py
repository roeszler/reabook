""" Import Modules """
from django.urls import path
from . import views


urlpatterns = [
    path('account/', views.login_user, name='login'),
    path('', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/<int:user_id>/', views.my_profile, name='my-profile'),
]
