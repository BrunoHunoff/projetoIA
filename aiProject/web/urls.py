from django.urls import path
from .views import interface



urlpatterns = [
    path('', interface, name='interface'),
]

