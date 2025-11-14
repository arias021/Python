# 6.Escribir un programa que pida por teclado un número al usuario y diga si es divisible por 3 o no.
numero = int(input("Introduce un numero: "))
if numero % 3 == 0:
    print('Es divisible el numero ' + str(numero) + ' a 3.')
else:
    print('No es divisible a 3 el numero ' + str(numero)+ ' a 3.')

