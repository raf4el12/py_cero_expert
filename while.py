numero = int(input('Por favor ingrese un numero: '))



while numero < 100:
    print(numero)
    numero *= 2
   


#comando = ""
#
#while comando.lower() != 'salir':
#    comando = input("$ ")
#    print(comando)


"""
LOOPS INFINITOS ES CUANDO NO TENEMOS UNA CONDICION DE SALIDA:
"""

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "Salir":
        break

"""
"""