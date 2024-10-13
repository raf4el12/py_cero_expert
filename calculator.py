n1 = int(input('Por favor ingrese un numero: '))
n2 = int(input('Por favor ingrese un numero: '))

print(n1 + n2)

# esto lo podemos hacer como una simple suma que lo queramos mostrar en pantalla 

"""
Ahora si queremos hacer una calculadora algo mas complejo pero simple hariamos algo como esto:
"""

sum = n1  + n2 
resta = n1 - n2
mult = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2},
el resultado de la suma es : {sum}
el resultado de la resta es : {resta}
el resultado de la multiplicacion es : {mult}
el resultado de la division es : {div}
"""

print(mensaje)