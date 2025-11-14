#Alberto Arias  EJERCICIO2      14/11/2025/Noviembre/Viernes
#Parte1

Mensaje = input('Pon tu mensaje secreto: ')
Palabra = input('Pon tu palabra de cifrado: ')
Numero = int (input('Pon tu clave numerica: '))
for letra in Palabra:
    PalabraCambiado = Palabra.replace(letra, str(Numero))
print(PalabraCambiado)

#Parte2

#  print(Palabra[0:2][3:5])
if Numero%2 == 0:
    print(Palabra.upper)
else:
    print(Palabra.lower)


