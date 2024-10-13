"""
Esta aplicacion lo que tiene que hacer es verificar si ya hemos ingresado un numero antes, en caso de que no hemos vamos a indicar al usuario que tiene que ingresar un numero
y bueno como siguiente paso tiene que ingresar la operacion que desee realizar y por ultimo tiene que ingresar otro numero,
despues de eso tenemos que mostrar el resultado y el resultado lo vamos a guardar en el primer numero y luego la siguiente operacion y con siguiente que ingrese el 2do numero
"""

print('Bienvenido a nuestra calculadora! ')
print('para salir del programa escriba Salir')
print('Tenemos las siguientes oepraciones:\n'
      'SUMA, RESTA, MULTIPLICACION Y DIVISION')


resultado = ''

while True:
    if not resultado:
        resultado = input('Ingrese un numero: ')
        if resultado.lower() == 'salir':
            break
        resultado = int(resultado)
## ingresar operacion 
    op = input('Ingrese una operacion: ')
    if op.lower() == "salir":
        break
    n2 = input('Pora favor ingrese un numero: ')
    if n2.lower() == 'salir':
        break
    n2 = int(n2)
### ahora vamosa a hacer las operaciones:
    if op.lower() == '+'or 'suma':
        resultado += n2
    elif op.lower() == '-' or 'resta':
        resultado -= n2
    elif op.lower() == '/' or 'division':
        resultado /= n2
    elif op.lower() == '*' or 'multiplicacion':
        resultado *= n2
    else:
        print('Operacion no valida!')
        break
    print(f'La {op} es {resultado}')