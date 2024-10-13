"""
Para hacer este ejercicio necesitaremos estos pasos:

crear una funcion para eliminar espacios en blanco de un string

funcion que tome un string y que aplique un reverse

"""


#def es_palindromo(texto):
#    texto_limpio = texto.replace(" ","").lower()
#
#    # usaremos el for para verificar si el texto es palindromo o no
#    long = len(texto_limpio)
#    for i in range (long // 2):
#        if texto_limpio[i] != texto_limpio[long - i - 1]:
#            return False
#        return True
#    
#
#
#teclado = input("Ingrese un texto para verificar si es palindromo o no: ")
#
#resultado = es_palindromo(teclado)
#
#if resultado:
#    print(F'"{teclado}" es un palindromo')
#else:
#    print(f'"{teclado}" no es un palindromo')



#def es_palindromo(texto):
#    texto_limpio=texto.replace(" ", "").lower()
#
#    ## ahora vamos a tener que verificar si es palindromo o no:
#    longitud = len(texto_limpio)
#    for i in range(longitud // 2):
#        if texto_limpio[i] != texto_limpio [longitud - i - 1]:
#            return False
#        return True
#
#teclado = input("Por favor ingresar texto para comprobar si es palindromo o no: ")
#
#resultado = es_palindromo(teclado)
#
#if resultado:
#    print(f'"{teclado}" es palindromo')
#else:
#    print(f'"{teclado}" no es palindromo')
#        


def no_space(texto):
    nuevo_texto =""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto



def reverse(texto):
    texto_reverse=""
    for char in texto:
        texto_reverse = char + texto_reverse
    return texto_reverse


resultado= reverse("holamundo")
print(resultado)


def es_palindromo(texto):
    texto = no_space(texto)
    texto_reverse = reverse(texto)
    return texto.lower() == texto_reverse.lower()



teclado=input("Por favor ingrese un texto para saber si es palindromo o no: ")

resultado = es_palindromo(teclado)

if resultado:
    print(f"{teclado} es palindromo")
else:
    print(f"{teclado} no es palindromo")










