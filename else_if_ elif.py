""""
EN ESTA SECCION APRENDEROS LO QUE SON LAS SETENCIAS IF, ELSE Y ELIF EN PYTHON

"""

print('Clase sentencia IF,ELSE,ELIF\n')

edad = int(input('Por favor ingresar su edad: '))


###  /!  MUY IMPORTANTE QUE LAS SENTENCIAS O EN ESTE CASO EVALUACIONES SIEMPRE EMPIEZAN DE ARRIBA HACIA BAJO  

if edad >= 50: # a la derecha siempre le podemos pasar la expresion que queramos siempre que queramos validar un TRUE o FALSE
    print(f'Por tener la edad de {edad} años, usted es beneficiario del descuento para adultos ') # importante siempre tabular para que el print corra dentro de la sent if 

elif edad >17:
    print(f'Puedes ver la pelicula porque usted es mayor de edad: ')

else: # LA INSTRUCCION DE ELSE NOS INDICARIA EL CASO CONTRARIO O POR ULTIMA OPCION COMO ALGO ASI DECIRLO
    print(f'Usted no cuenta con la edad suficiente ya que es menor de edad con {edad}')





