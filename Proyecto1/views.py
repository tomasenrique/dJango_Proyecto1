"""
Este archivo sera una vista que se llamara para poder mostrar datos en la vista web.
Los metodos aqui son basicos y no tiene parametro de entreda.

"""

from django.http import HttpResponse  # Para poder pasar paginas y datos, ejm saludo6
import datetime
# from django.template.loader import get_template  # Asi se llama al metodo 'get_template' para usar muchos templates
from django.template import Template, Context  # para poder usar las plantilla y su contexto

# Este es un ejm de como pasar html
# Este sera su enlaca en la web ==>> http://localhost:8000/saludo/
#
# def saludo(request):  # primera vista
#     return HttpResponse("""
#     <html>
#         <body>
#             <h1>Hola a todos mi primera pagina con django</h1>
#         </body>
#     </html>""")

# Este es otro ejm de pasar html - Video 3
documento = """ <html>
                    <body>
                        <h1 style="color:#00f; text-align:center">Hola a todos mi primera pagina con django</h1>
                    </body>
                </html>"""

"""Primera vista, OJO => Para poder acceder a esta vista desde la web hay que declararla en el 'urls.py'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),  # Aqui se le pasa el url(saludo) para llamarlo por vista 'saludo' en la web
] """


# Este sera su enlaca en la web ==>> http://localhost:8000/saludo/
def saludo(request):
    return HttpResponse(documento)


#  Este sera su enlaza en la web ==>> http://localhost:8000/despedida/
def despedida(request):
    return HttpResponse("Hasta luego people.")


# ======================================================================================================================
# ======================================================================================================================
# Video 3
# Muestra la fecha del sistema
# Este sera su enlaza en la web ==>> http://localhost:8000/fecha/
def dame_fecha(request):
    dame_actual = datetime.datetime.now()  # Obtiene la fecha del sistema
    documento_fecha = """ <html>
                              <body>
                                    <h1>Fecha y hora actuales: %s</h1>
                              </body>
                          </html>""" % dame_actual
    return HttpResponse(documento_fecha)


# ======================================================================================================================
# ======================================================================================================================
# Video 4
# Aqui se le esta pasando un parametro 'anyo' para que este se reciba en la url path
# Este sera su enlaza en la web ==>> http://localhost:8000/cal_edad1/1990
def calcula_edad1(request, anyo):
    edad_actual = 40
    periodo = anyo - 2020
    edad_futura = edad_actual + periodo

    documento_fecha = """ <html>
                          <body>
                              <h1>En el año %s tendrás %s</h1>
                          </body>
                      </html>""" % (anyo, edad_futura)
    return HttpResponse(documento_fecha)


# Aqui se pasan dos parametros para que los reciba la url del path
# Este sera su enlaza en la web ==>> http://localhost:8000/cal_edad2/21/2000
def calcula_edad2(request, edad, anyo):
    edad_actual = edad
    periodo = anyo - 2020
    edad_futura = edad_actual + periodo

    documento_fecha = """ <html>
                          <body>
                              <h1>En el año %s tendrás %s</h1>
                          </body>
                      </html>""" % (anyo, edad_futura)
    return HttpResponse(documento_fecha)

# ======================================================================================================================
# ======================================================================================================================
