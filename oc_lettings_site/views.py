from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def index(request: HttpRequest) -> HttpResponse:
    """
    Display the home page of the Holiday Homes website.

    Args:
        request (HttpRequest): The HTTP request sent by the user.

    Returns:
        HttpResponse: The rendered HTML response of the home page.
    """

    logger.info("Home page accessed")
    return render(request, 'index.html')


def custom_404(request: HttpRequest, exception) -> HttpResponse:
    """
    Custom 404 error handler when the urls schema is not parameterized.

    Args:
        request (HttpRequest): The HTTP request sent by the user.
        exception: The exception that triggered the 404 error.

    Returns:
        HttpResponse: The rendered HTML response for the 404 error page.
    """
    logger.warning(f"404 error at {request.path}")
    return render(request, '404.html', status=404)


def custom_500(request: HttpRequest) -> HttpResponse:
    """
    Custom 500 error handler.

    Args:
        request (HttpRequest): The HTTP request sent by the user.

    Returns:
        HttpResponse: The rendered HTML response for the 500 error page.
    """
    logger.critical("500 internal server error")
    return render(request, '500.html', status=500)
