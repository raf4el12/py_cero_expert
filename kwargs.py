"""
Ahora vamos a utilizar lo que son los keywords arguments, cuando queremos trabajar
con los kwargs tenemos que utilizar dos ** antes del parametro 
que asignaremos
"""


def get_product(**datos):  ## es como si trabajaramos con un diccionario
    print(datos["id"], datos["marca"])


get_product(id = 2,
            desc = "Esto es un iphone",
            marca = "Iphone")


def get_estudiante(**datos):
    print(datos["nombre"], datos ["apellido"])

get_estudiante(nombre="Rafael",
               apellido="Ardiles",
               edad=12,
               colegio="San Martin de Porres")
