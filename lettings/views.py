from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Letting


def index(request: HttpRequest) -> HttpResponse:
    """
    Display a list of all lettings.

    Args:
        request (HttpRequest): The HTTP request sent by the user.

    Returns:
        HttpResponse: The rendered lettings index page.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}

    return render(request, 'lettings/index.html', context)


def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    """
    Display a specific letting.

    Args:
        request (HttpRequest): The HTTP request sent by the user.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: The rendered HTML response for the letting detail page.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }

    return render(request, 'letting.html', context)
