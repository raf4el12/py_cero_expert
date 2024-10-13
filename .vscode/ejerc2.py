"""
Para hacer este ejercicio necesitaremos estos pasos:

crear una funcion para eliminar espacios en blanco de un string

funcion que tome un string y que aplique un reverse

"""


def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto): 
    texto_reverse = ""
    for char in texto:
        texto_reverse = char + texto_reverse
    return texto_reverse


def es_palindromo(texto):
    texto = no_space(texto)
    texto_reverse = reverse(texto)
    return texto.lower() == texto_reverse.lower()


r = input("Por favor ingrese un texto para saber si es palindromo o no: ")

resultado= es_palindromo(r)

if resultado:
    print(f"{r} es palindromo")
else:
    print(f"{r} no es palindromo")
