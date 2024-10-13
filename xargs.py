def suma(*numeros):
    resultado = 0
    for numero in numeros: ## estamos iterando para que x cantidad de numeros sea x cantidad de los parametros que coloquemos
        resultado += numero
    print(f"El resultado es {resultado}")
    


n1 = int(input("Ingresar primer numero: "))
n2 = int(input("Ingresar segundo numero: "))

resultado = suma (n1,n2,4,1)


