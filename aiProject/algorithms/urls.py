from django.urls import path
from .views import ucs

urlpatterns = [
    path('ucs/', ucs, name='ucs'),
]
