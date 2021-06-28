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
from Proyecto1.views import saludo, despedida, dame_fecha, calcula_edad1, calcula_edad2, saludo2, saludo3, saludo4, \
    saludo5, saludo5_1, saludo6,saludo7


"""
NOTA:
    path(dato1, dato2),

Donde:
    dato1 = Sera el nombre(personalidado), por el cual llamaremos al metodo de la vista(view) en la pagina web, tambien 
            se puede agregar parametros para los metodos.
    dato2 = Sera el nombre del metodo(view) 

EJM ==>> path('fecha/', dame_fecha),  """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),  # Aqui se le pasa el url(saludo) para llamarlo por vista 'saludo' en la web
    path('despedida/', despedida),  # El primer parametro el nombre de la url y el segundo es el nombre de la funcion
    path('fecha/', dame_fecha),  # Para agregar el metodo para mostrar la fecha y hora del sistema.
    path('cal_edad1/<int:anyo>', calcula_edad1),  # Aqui se pasa un valor en el enlace 'calcula_edad/<int:anyo>'
    path('cal_edad2/<int:edad>/<int:anyo>', calcula_edad2),  # Aqui se pasa 2 parametros
    path('saludo2/', saludo2),  # para usar con plantilla
    path('saludo3/', saludo3),  # Para pasar datos a la plantilla
    path('saludo4/', saludo4),  # Para pasar datos usando una clase creada
    path('saludo5/', saludo5),  # Para pasar una lista con datos
    path('saludo5_1/', saludo5_1),  # Para probar un condicional y filtros
    path('saludo6/', saludo6),  # Para mostrar datos en los templates usando el archivo setting.py
    path('saludo7/', saludo7),  # Usando 'shortcuts' con el metodo simpleificado render()
]
