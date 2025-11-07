from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Profile


def index(request: HttpRequest) -> HttpResponse:
    """
    Display a list of all profiles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered profiles index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}

    return render(request, 'profiles/index.html', context)


def profile(request: HttpRequest, username: str) -> HttpResponse:
    """
    Display a specific user profile.

    Args:
        request (HttpRequest): The HTTP request sent by the user.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: The rendered HTML response for the profile detail page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}

    return render(request, 'profile.html', context)
