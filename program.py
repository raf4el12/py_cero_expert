"""
Esta aplicacion lo que tiene que hacer es verificar si ya hemos ingresado un numero antes, en caso de que no hemos vamos a indicar al usuario que tiene que ingresar un numero
y bueno como siguiente paso tiene que ingresar la operacion que desee realizar y por ultimo tiene que ingresar otro numero,
despues de eso tenemos que mostrar el resultado y el resultado lo vamos a guardar en el primer numero y luego la siguiente operacion y con siguiente que ingrese el 2do numero
"""

print("BIENVENIDO A NUESTRA CALCULADORA! ")
print("Si desea salir del programa escriba !salir")
print("Contamos con las siguientes operaciones \n"
      "suma, resta, division, multiplicacion")

resultado = ""

while True:
    if not resultado:
        resultado = input("Por favor ingresar un numero: ")
        if resultado.lower() == "!salir":
            break
        resultado = int(resultado)
    
    op = input("Por favor ingrese una operacion: ")
    if op.lower() == "!salir":
        break
    
    n2 = input ("Por favor ingresar 2do numero: ")
    if n2.lower() == "!salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicacion":
        resultado *= n2
    elif op.lower() == "division":
        resultado /= n2
    else:
        print(f"{op} no es valido para hacer una operacion!")
        break

    print(f"El resultado es {resultado}")

