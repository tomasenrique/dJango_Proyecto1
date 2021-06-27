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
# PLANTILLAS 1
# Aqui se cargara una plantilla al metodo que actua como una vista

# Este sera su enlaza en la web ==>> http://localhost:8000/saludo2
def saludo2(request):
    # doc_externo = open("C:\D\Lenguajes\Django\proyecto1\proyecto1\templates\miplantilla.html")  # Se carga la plantilla
    doc_externo = open("D:/Lenguajes/Django/Proyecto1/Proyecto1/templates/miplantilla.html")  # Se carga la plantilla

    plt = Template(doc_externo.read())  # Se crea un objeto de tipo templates para cargar la plantilla
    doc_externo.close()  # Se cierra el documento

    ctx = Context()  # Se crea el contexto para la plantilla

    documento_p = plt.render(ctx)  # se crea el renderizado de la pagina y se le pasa el contexto

    return HttpResponse(documento_p)


# D:\Lenguajes\Django\Proyecto1\Proyecto1\templates

# ======================================================================================================================
# ======================================================================================================================

# PLANTILLAS 2

#  Aqui se trabajara con templates dinamicas

# Este sera su enlaza en la web ==>> http://localhost:8000/saludo3
def saludo3(request):
    nombre = "tomas"
    apellido = "estrada"
    mi_fecha = datetime.datetime.now()

    doc_externo = open("D:/Lenguajes/Django/Proyecto1/Proyecto1/templates/miplantilla2.html")  # Se carga la plantilla

    plt = Template(doc_externo.read())  # Se crea un objeto de tipo templates para cargar la plantilla
    doc_externo.close()  # Se cierra el documento

    # Se crea el contexto para la plantilla y un diccionario para poder pasar los datos del servidor
    # a la pagina miplantilla2.html(vista)
    # Se unsa un diccionario  de 'clave:valor' para pasar los datos a a vista, donde:
    #
    # nombre_persona => Sera el nombre que se le da a la variable al enviarla a la vista y la forma de invocarla.
    # nombre => Sera el nombre de la variable que se quiere enviar a la vista.
    diccionario1 = {"nombre_persona": nombre, "apellido": apellido, "fecha": mi_fecha}
    ctx = Context(diccionario1)

    documento_p = plt.render(ctx)  # se crea el renderizado de la pagina y se le pasa el contexto

    return HttpResponse(documento_p)


# ===========================================================
#  Trabajando con una clase para pasarle los valores a la pagina

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# Este sera su enlaza en la web ==>> http://localhost:8000/saludo4
def saludo4(request):
    p1 = Persona("Enrique", "Torres")

    mi_fecha = datetime.datetime.now()

    doc_externo = open("D:/Lenguajes/Django/Proyecto1/Proyecto1/templates/miplantilla2.html")  # Se carga la plantilla

    plt = Template(doc_externo.read())  # Se crea un objeto de tipo templates para cargar la plantilla
    doc_externo.close()  # Se cierra el documento

    # Se crea el contexto para la plantilla y un diccionario para poder pasar los datos a la pagina miplantilla2.html
    diccionario1 = {"nombre_persona": p1.nombre, "apellido": p1.apellido, "fecha": mi_fecha}
    ctx = Context(diccionario1)

    documento_p = plt.render(ctx)  # se crea el renderizado de la pagina y se le pasa el contexto

    return HttpResponse(documento_p)

# ======================================================================================================================
# ======================================================================================================================
# PLANTILLAS 3

#  Aqui se pasaran listas de datos a la pagina

# Este sera su enlaza en la web ==>> http://localhost:8000/saludo5
def saludo5(request):
    p2 = Persona("Luis", "Silva")
    lista1 = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    lista2 = []

    mi_fecha = datetime.datetime.now()

    doc_externo = open("D:/Lenguajes/Django/Proyecto1/Proyecto1/templates/miplantilla3.html")  # Se carga la plantilla
    plt = Template(doc_externo.read())  # Se crea un objeto de tipo templates para cargar la plantilla
    doc_externo.close()  # Se cierra el documento

    # Se crea el contexto para la plantilla y un diccionario para poder pasar los datos a la pagina miplantilla2.html
    diccionario1 = {"nombre_persona": p2.nombre, "apellido": p2.apellido, "fecha": mi_fecha, "lista1": lista1,
                    "lista2": lista2}
    ctx = Context(diccionario1)

    documento_p = plt.render(ctx)  # se crea el renderizado de la pagina y se le pasa el contexto

    return HttpResponse(documento_p)
