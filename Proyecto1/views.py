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

# Este es otro ejm de pasar html
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

