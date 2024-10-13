"""
Esta aplicacion lo que tiene que hacer es verificar si ya hemos ingresado un numero antes, en caso de que no hemos vamos a indicar al usuario que tiene que ingresar un numero
y bueno como siguiente paso tiene que ingresar la operacion que desee realizar y por ultimo tiene que ingresar otro numero,
despues de eso tenemos que mostrar el resultado y el resultado lo vamos a guardar en el primer numero y luego la siguiente operacion y con siguiente que ingrese el 2do numero
"""


print('Bienvenidos a la calculadora\n')
print('Para salir escribe Salir')
print('Las operaciones que presenta la calculadora son: Suma, resta, multi y division.')

resultado = ''

while True:
    if not resultado:
        resultado = input('Ingrese numero:')
        if resultado.lower() == "Salir":
            break
        resultado = int(resultado)
    op = input('Ingresa operacion:')
    if op.lower() == 'Salir':
        break
    n2 = input('Ingrese siguiente numero:')
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == 'suma':
        resultado += n2
    elif op.lower() == 'resta':
        resultado -= n2
    elif op.lower() == 'multi':
        resultado *= n2
    elif op.lower() == 'division':
        resultado /= n2
    else:
        print('Operacion no valida!')
        break

    print(f'El resultado es {resultado}')
    


    


