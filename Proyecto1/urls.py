"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# Aqui se importa el metodo creado
from Proyecto1.views import saludo, despedida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),  # Aqui se le pasa el url(saludo) para llamarlo por vista 'saludo' en la web
    path('despedida/', despedida),  # El primer parametro el nombre de la url y el segundo es el nombre de la funcion
]
