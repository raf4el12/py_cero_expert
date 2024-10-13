"""
EN ESTA CLASE VAMOS A VER LO QUE SON LAS FUNCIONES

"""
#
#def hola():
#    print("Hola mundo")
#    print("Hola python ")
#
#hola()
#
#
#
## Función que suma dos números
#def sumar(a, b):
#    return a + b
#
## Llamando a la función y guardando el resultado
#a = int(input("NUMERO 1: "))
#b = int(input("NUMERO 2: "))
#
#resultado = sumar(a,b)
#print(resultado)

def saludar(nombre="no ingreso nombre", apellido="no ingreso apellido"):  ## estos parametro ingresados son obligatorios llenar!!!
    print(f"Es un gusto saludarte {nombre} {apellido}")


name = input("Por favor ingrese su nombre: ")
add = input ("Por favor ingrese su apellido: ")

saludar(name, add)
saludar(nombre=name, apellido = add)
saludar(apellido= "ardiles", nombre = "Hector")


