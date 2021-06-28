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


# ======================================================================================================================
# PLANTILLAS 4

#  Aqui se pasaran listas de datos a la pagina

# Este sera su enlaza en la web ==>> http://localhost:8000/saludo5_1
def saludo5_1(request):
    p2 = Persona("Luis", "Silva")
    lista1 = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    mi_fecha = datetime.datetime.now()

    doc_externo = open("D:/Lenguajes/Django/Proyecto1/Proyecto1/templates/miplantilla4.html")  # Se carga la plantilla
    plt = Template(doc_externo.read())  # Se crea un objeto de tipo templates para cargar la plantilla
    doc_externo.close()  # Se cierra el documento

    # Se crea el contexto para la plantilla y un diccionario para poder pasar los datos a la pagina miplantilla2.html
    diccionario1 = {"nombre_persona": p2.nombre, "apellido": p2.apellido, "fecha": mi_fecha, "lista": lista1}
    ctx = Context(diccionario1)

    documento_p = plt.render(ctx)  # se crea el renderizado de la pagina y se le pasa el contexto

    return HttpResponse(documento_p)


# ======================================================================================================================
# ======================================================================================================================
# PLANTILLAS 5 - CARGADORES DE PLANTILLAS

"""Aqui se vera como cargar una o varias templates de forma mas optima para no usar 'close()' o el 'open()' que son 
metodos que estan consumiento muchos recursos.

Para ello hay que ir al archivo 'setting.py' y buscar la lista 'TEMPLATES' y dentro de el se vera otra lista interna
llamada 'DIRS' que aqui se contendra todos los directorios que contengan las paginas web(plantillas - templates) 

Usando esta forma se ahorra varias lineas de codigo y se optimiza todo ya que aqui ya no se usaria un contexto
"""
from django.template import loader  # Esto es para poder cargar las plantillas (templates) => metodo saludo6


# Este sera su enlaza en la web ==>> http://localhost:8000/saludo6
def saludo6(request):
    p3 = Persona("Esther", "Galdeano")
    lista1 = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    lista2 = []

    mi_fecha = datetime.datetime.now()

    # Aqui se ubica el template por medio del archivo 'setting.py' y el metodo indicado
    doc_externo = loader.get_template('miplantilla5.html')

    # Se crea el contexto para la plantilla y un diccionario para poder pasar los datos a la pagina miplantilla2.html
    diccionario1 = {"nombre_persona": p3.nombre, "apellido": p3.apellido, "fecha": mi_fecha, "lista1": lista1,
                    "lista2": lista2}

    documento_p = doc_externo.render(diccionario1)  # se crea el renderizado de la pagina y se le pasa el contexto

    return HttpResponse(documento_p)

# ======================================================================================================================
# ======================================================================================================================
# PLANTILLAS 6 - PAQUETE SHORTCUTS Y COMO INCRUSTAR PLANTILLAS

""" USANDO PAQUETE SHORTCUTS
    Uso del paquete 'shortcuts' con el metodo render() para simpleificar los trabajos
    pagina => https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/

    Metodo => render(request, template_name, context=None, content_type=None, status=None, using=None)
    Donde los 2 siguentes son los mas usados:
    request: Argumento obligatorio
    template_name: La pagina web

    Usando este metodo se optimisaria el codigo, ver le metodo saludo6 y compara con el saludo7
"""

from django.shortcuts import render  # para usar el metodo render()


def saludo7(request):
    p4 = Persona("Federica", "Berti")
    lista1 = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    lista2 = []

    mi_fecha = datetime.datetime.now()

    # Se crea el contexto para la plantilla y un diccionario para poder pasar los datos a la pagina miplantilla2.html
    diccionario1 = {"nombre_persona": p4.nombre, "apellido": p4.apellido, "fecha": mi_fecha, "lista1": lista1,
                    "lista2": lista2}

    return render(request, "miplantilla6.html", diccionario1)


# ==================================================
""" USANDO PLANTILLAS INCRUSTADAS
    ver archivo barra.html y miplantilla6.html para obserbar el ejemplo de como insertar la plantilla

"""

# ======================================================================================================================
# ======================================================================================================================
# PLANTILLAS 7 - HERENCIA DE PLANTILLAS

""" Ver los archivos:
    plantillaBase.html, plantilla1.html, plantilla2.html
"""


def plantilla1(request):
    fecha_actual = datetime.datetime.now()  # Obtiene la fecha del sistema
    diccionario2 = {"dame_fecha": fecha_actual}
    return render(request, "herencia/plantilla1.html", diccionario2)


def plantilla2(request):
    fecha_actual = datetime.datetime.now()  # Obtiene la fecha del sistema
    diccionario2 = {"dame_fecha": fecha_actual}
    return render(request, "herencia/plantilla2.html", diccionario2)