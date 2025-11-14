
# 8. Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros(puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos intereses de ningún tipo y redondeamos a dos decimales.


importe_total = float(input('Dime cuanto tienes que pagar: '))
meses_totales = int(input('Dime en cuanto meses quieres fraccionarlo: '))
pago_al_mes = round(importe_total/meses_totales,2)
print(pago_al_mes)
