"""
URL configuration for Quiroz_B_IEI170 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Quiroz_B_IEI170_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('listar/', views.listar_reservas, name='listar_reservas'),
    path('agregar/', views.agregar_reserva, name='agregar_reserva'),
    path('modificar/<int:pk>/', views.modificar_reserva, name='modificar_reserva'),
    path('eliminar/<int:pk>/', views.eliminar_reserva, name='eliminar_reserva'),
]
