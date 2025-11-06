from django.urls import path
from . import views

app_name = 'profiles'  # namespace declaration

urlpatterns = [
    path('', views.index, name='index'),  # old profiles_index
    path('<str:username>/', views.profile, name='profile'),
    ]
