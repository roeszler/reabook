""" Import Modules """
from django.shortcuts import render


def view_blogs(request):
    """
    View to render the blogs page
    Looks within the current directory app_blog/templates/blog/blog.html
    """
    return render(request, 'blog/blog.html')
