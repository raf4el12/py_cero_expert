"""
Esta aplicacion lo que tiene que hacer es verificar si ya hemos ingresado un numero antes, en caso de que no hemos vamos a indicar al usuario que tiene que ingresar un numero
y bueno como siguiente paso tiene que ingresar la operacion que desee realizar y por ultimo tiene que ingresar otro numero,
despues de eso tenemos que mostrar el resultado y el resultado lo vamos a guardar en el primer numero y luego la siguiente operacion y con siguiente que ingrese el 2do numero
"""


print('BIENVENIDO A NUESTRA CALCULADORA!')
print('Si desea salir del programa escriba !salir')
print('Las operaciones que tiene son:\n'
      'suma, resta, multiplicacion, division')


resultado  = ''

while True:
    if not resultado:
        resultado = input('INGRESE NUMERO:')
        if resultado.lower() == '!salir':
            break
        resultado = int(resultado) 
    op = input('POR FAVOR INGRESE OPERACION!:')
    if op.lower() == '!salir':
        break
    n2 = input('INGRESE NUMERO:')
    if n2.lower() == '!salir':
        break
    n2 = int(n2)
    
    if op.lower() == 'suma':
        resultado += n2
    elif op.lower() == 'resta':
        resultado -= n2
    elif op.lower() == 'multiplicacion' :
        resultado *= n2
    elif op.lower() == 'division':
        resultado  /= n2
    else:
        print(f'La operacion ingresada {op} no es valida!')
        break
    print(f'El resultado de la {op} es {resultado}')


