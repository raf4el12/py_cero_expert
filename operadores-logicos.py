# El tipo logico AND reprenseta a que los dos valores de las condicionales
# tienen que ser true


# El tipo logico OR es uno de dos

gas = False

encendido = True

edad = int(input('Por favor ingrese su edad: '))

if not gas and encendido or edad > 17:
    print('Pudes avannzar')
    

if edad >= 18 and edad <= 65:
    print('Usted pruede entrar a la piscina')
else:
    print('No puede entrar a la piscina')



#if 18 >= edad  <= 65:
#    print('Usted puede entrar a la piscina')
#else:
#    print('No puede entrar a la piscina')
#
