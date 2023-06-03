from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('agregar', views.agregar),
    path('nuevaMascota', views.nuevaMascota),
    path('edicion/<codigo>', views.edicion),
    path('editar', views.editar),
    path('eliminar/<codigo>', views.eliminar),
]