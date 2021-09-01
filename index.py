# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# =============================================================================
# # PUNTO 1
# # CALCULAMOS EL VALOR DE Y
# =============================================================================
print("Vamos a calcular el valor de Y")
y = float((5 + 2 - 5)**2 * 5 + 8) / (2 - 30) / 2 * 5 - 3
print('Separamos primero los valores en parentecis ((5 + 2 - 5)^2 * 5 + 8) ')
print('Luego dividimos el resultado con (2 - 30)')
print('Por ultimo realice la operacion de: / 2 * 5 - 3')
print('resultado del punto 1 es: ',y)
# FIN DEL PRIMER PUNTO

# =============================================================================
# PUNTO 2
# CALCULAMOS EL VALOR DE Y
# =============================================================================
z = 5
n = 3
m = int(z)-int(n)

y = float((((int(z) + 2 - int(n))^2*int(m))+8/2-30) / 2 * 5  - 3)
exp = float(pow(y, 5))
res = float(float(exp)+15*3-9)/3

print('Resultado del punto 2:',res)
# FIN DEL SEGUNDO PUNTO

# =============================================================================
# # PUNTO 3
# # CALCULAMOS EL VALOR DE Y
# =============================================================================
z = 5
n = float((8 + 2 - 4 ) ** 2 * 5 + 8 +7/2 - 30 * 5) / 2 * 5 - 3 
m = float(z ** 2 * 3 + n) 
y = float((((z + 2 - n ) ** 2 * m + 8 / 2 - 30) / 2 * 5 - 3) ** 5 + 15 * 3 - 9/3) ** 2 - 5/4
print('Resultado del punto 3 es: ',y)
# FIN DEL TERCER PUNTO

# =============================================================================
# # Haga un algoritmo que calcule la masa de la siguiente fórmula:
# # Masa = (presión * volúmen) / (0.37 * (temperatura + 460))
# # Primer Punto
# =============================================================================
p = float(input('Ingresa la presion: '))
v = float(input('Ingresa el volumen: '))
t = float(input('Ingresa la temperatura: '))
m = float((p * v) / (0.37 * (t + 460)))

print('El resultado de la masa es de: ',m)

# =============================================================================
# Calcular el número de pulsaciones que una persona debe tener por
# cada 10 segundos de ejercicio, si la fórmula es:
# Num. Pulsaciones = (200 – edad) /10.
# =============================================================================
edad = float(input('Ingresa su Edad: '))
p = (200 - edad) / 10

print('Su numero de pulsaciones es: ',p)

# =============================================================================
# Tres personas deciden invertir su dinero para fundar una empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
# que cada quien invierte con respecto a la cantidad total invertida.
# =============================================================================
inver1 = int(input('Ingresa primera inversion: '))
inver2 = int(input('Ingresa segunda inversion: '))
inver3 = int(input('Ingresa tercera inversion: '))
suma = inver1 + inver2 + inver3
porcentaje1 = float((inver1 / suma)) * 100
porcentaje2 = float((inver2 / suma)) * 100
porcentaje3 = float((inver3 / suma)) * 100

print('Total Invertido: ',suma)
print('Porcentaje invertido persona1: ',porcentaje1)
print('Porcentaje invertido persona2: ',porcentaje2)
print('Porcentaje invertido persona3: ',porcentaje3)

# =============================================================================
# 4. Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final.
# =============================================================================
saldoI = int(input('Ingresa saldo inicial: '))
saldoF = int(saldoI * 1.5) 
print('Saldo final es de: ',saldoF)

# =============================================================================
# Una empresa le hace los siguientes descuentos sobre el sueldo base
# a sus trabajadores: 1% por ley de politica pública, 4% por seguro
# social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un algoritmo que determine el monto de cada descuento y el monto total
# a pagar al trabajador
# =============================================================================
sueldoB = int(input('Ingrese sueldo base: '))
ley = sueldoB * 0.01
seguro = sueldoB * 0.04
seguroF = sueldoB * 0.005
cajaH = sueldoB * 0.05
suma = ley + seguro + seguroF + cajaH 
total = sueldoB - suma
print('ley de politica pública: ',ley)
print('Seguro Social: ',seguro)
print('Seguro Forzoso: ',seguroF)
print('Caja de ahorro: ',cajaH)
print('Sueldo total: ',total)

# =============================================================================
# El periódico el Informador cobra por un aviso clasificado un monto
# que depende del número de palabras, tamaño en cetímetros y
# número de colores. Cada palabra tiene un costo de $20.000, cada
# centímetro tiene un costo de $15.000 y cada color tiene un costo de
# $25.000. Realice un algoritmo que determine el monto a pagar por un
# aviso clasificado.
# =============================================================================
palabra = int(input('Cantidad de palabra de su anuncio: '))
tamaño = float(input('Tamaño de su anuncio en cm: '))
color = int(input('Cantidad de colores de su anuncio: '))
t1 = int(palabra * 20000)
t2 = int(tamaño * 25000)
t3 = int(color * 15000)
total = t1 + t2 + t3
print('Total a pagar por su anuncio: ',total)
