"""proj_reabook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import error_404_view

urlpatterns = [
    path('', include('app_home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('diary/', include('django.contrib.auth.urls')),
    path('diary/', include('app_diary.urls')),
    path('book/', include('app_bookings.urls')),
    path('properties/', include('app_properties.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# add a flag for
# handling the 404 error
error_404_view = 'proj_reabook.views.error_404_view' # noqa
