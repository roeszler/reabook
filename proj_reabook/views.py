""" Import Modules """
from django.shortcuts import render


def error_404_view(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)
