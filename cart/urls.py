# cart/urls.py

from django.urls import path
from . import views

app_name = 'cart'  # Esto establece el espacio de nombres para las URLs de la aplicación

urlpatterns = [
    path('carts/', views.carts, name='carts'),
]