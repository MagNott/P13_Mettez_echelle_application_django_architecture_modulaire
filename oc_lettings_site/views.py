from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """
    Display the home page of the Holiday Homes website.

    Args:
        request (HttpRequest): The HTTP request sent by the user.

    Returns:
        HttpResponse: The rendered HTML response of the home page.
    """

    return render(request, 'index.html')
