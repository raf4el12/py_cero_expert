""" Supongamos que tenemeos un listado de estudiantes que tienen nombre y apellido
    y queremos crear un campo nuevo de NOMBRE COMPLETO 
    
"""

#names = {'Rafael', 'Sebastian', 'Rene'}
#for nombes in names:
#    print(nombes)
#
#
#for numero in range (5):
#    print(numero, numero * "Rafael Hola")




numero_buscar = int(input('Por favor ingrese numero a buscar:'))


for numeros in range (10):
    print(numeros)
    if numeros == numero_buscar:
        print(f"Se encontro el numero encontrado {numero_buscar}")
        break
else:
        print(f"NO se encontro el numero {numero_buscar}")


### TAMBIEN PODEMOS ITERAR CADENAS DE TEXTOS CON EL FOR 

cadena = 'Hola Python'

for i in cadena:
     print(i)
