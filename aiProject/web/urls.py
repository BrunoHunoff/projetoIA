from django.urls import path
from .views import pagina_teste

urlpatterns = [
    path('teste/', pagina_teste, name='pagina_teste'),
]
