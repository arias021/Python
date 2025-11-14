#7. Escribir un programa que pida un número por teclado al usuario que simule ser el precio de
#un artículo y escriba el resultado de aplicarle el IVA del 21%
precio = float (input('Dime un precio: '))
precio_final = precio * 1.21
print('IVA ' + str(precio * 0.21))
print('Precio + IVA ' + str(precio_final))