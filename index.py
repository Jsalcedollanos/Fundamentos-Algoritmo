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
ley = int(sueldoB * 0.01)
seguro = int(sueldoB * 0.04)
seguroF = int(sueldoB * 0.005)
cajaH = int(sueldoB * 0.05)
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

# =============================================================================
# Una empresa paga a sus empleados un bono por antigüedad que
# consiste en $100.000 por el primer año laboral y $120.000 por cada
# año siguiente. Realice un algoritmo que determine el monto del bono
# a pagar a un trabajador que tiene varios años en la empresa
# =============================================================================
año = int(input('Ingrese los años trabajados: '))
if año == 1:
    bono = 100000
    print('Su bono es  de: ',bono)
    
if año > 1:
    bono1 = 100000
    bono2 = (año - 1) * 120000
    total = bono1 + bono2
    print('Su bono es  de: ',total)

# =============================================================================
# Una Universidad le paga a sus profesores $20.000 la hora y le hace
# un descuento del 5% por concepto de caja de ahorro. Determine el
# monto del descuento y el monto total a pagar al profesor.
# =============================================================================
hora = int(input('Ingrese horas trabajadas: '))
hora_paga = int(hora * 20000)
descuento = int(hora_paga * 0.05)
total_pagado = int(hora_paga - descuento)

print('Descuento: ',descuento)
print('Total a pagar: ',total_pagado)

# =============================================================================
# Un centro de comunicaciones alquilan tarjetas para realizar llamadas
# y cobran el monto consumido de la tarjeta mas un recargo del 20%.
# Teniendo como dato de entrada el monto inicial y el monto final de la
# tarjeta, determine el costo de la llamada.
# =============================================================================
monto_inicial = int(input('Ingrese monto Inicial: '))
monto_final = int(input('Ingrese monto Final: '))
monto_consumido = int(monto_inicial - monto_final) 
recargo = monto_consumido * 0.2
print('Costo de la llamada: ',recargo)

# =============================================================================
# En una fototienda cobran por el revelado de un rollo $1.500 por cada
# foto. Realice un algoritmo que determine el monto a pagar por un
# revelado completo sabiendo que adiconalmente le cobran el IVA
# (16%).
# =============================================================================
cantidad_foto = int(input('Ingrese cantidad de fotos a revelar: '))
valor = int(cantidad_foto * 1500)
iva = int(valor * 0.16)
total_pagar = int(valor + iva)
print('Iva: ',iva)
print('valor a pagar: ',total_pagar)

# =============================================================================
# 11. En un hospital existen tres áreas: Ginecología, Pediatría y
# Traumatología. El presupuesto anual del hospital se reparte
# conforme a la siguiente tabla:
# Area Porcentaje Presupuestal
# Ginecología 40%
# Traumatología 30%
# Pediatría 30%
# Obtener la cantidad de dinero que recibirá cada área, para cualquier
# monto presupuestal.
# =============================================================================
monto = int(input('Ingrese Monto presupuestal: '))
ginecologia = int(monto * 0.4)
traumatologia = int(monto * 0.3)
pediatria = int(monto * 0.3)
print('Monto presupuestal para ginecologa: ',ginecologia)
print('Monto presupuestal para traumatologia: ',traumatologia)
print('Monto presupuestal para pediatria: ',pediatria)

# =============================================================================
# Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
# que consiste en dejar gratis el alquiler de una película. Realice un
# algoritmo que teniendo como dato de entrada el total de películas
# alquiladas, y el número de días de alquiler, determine el monto a
# pagar.
# =============================================================================
cantidad_pelicula = int(input('Ingrese cantidad de peliculas: '))
cantidad_dia = int(input('Ingresa cantidad de dias: '))
valor_dia = cantidad_dia * 1500
total_pagar = cantidad_pelicula * valor_dia
print('Cantidad a pagar: ',total_pagar)

# =============================================================================
# Una Agencia de viajes cobra por un Tour a Cartagena $25.000
# diarios por persona. Realice un algoritmo que determine el monto a
# pagar por una familia que desee realizar dicho Tour sabiendo que
# también cobran el 12% de IVA.
# =============================================================================
dia = int(input('Ingrese cantidad de dias: '))
cantidad_persona = int(input('Ingrese cantidad de miembros de familia: '))
pago_diario = cantidad_persona * 25000
pago = pago_diario * dia
iva = pago * 0.12
total = pago + iva
print('Total a pagar mas iva es: ',total)

# =============================================================================
# Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
# clientes. Cobra por una habitación $100.000 el primer día y por el
# resto $200.000 por día. Realice un algoritmo que determine el valor
# total a pagar por la habitación si la estadía fue de varios días.
# =============================================================================
cantidad_dia = int(input('Ingrese cantidad de dias: '))
if cantidad_dia < 1:
    print('Monto digitado inferior a 1!')
if cantidad_dia == 1:
    total = cantidad_dia * 100000
    print('Cantidad a pagar es: ',total)
if cantidad_dia > 1:
    total = cantidad_dia * 200000 - 100000
    print('Cantidad a pagar es: ',total)
    
# =============================================================================
# El banco del Pueblo da microcréditos a empresarios para ser
# cancelados en un lapso de 2 años (24 meses). Al monto del
# préstamo se le cobra un interés del 24%. El empresario debe pagar
# la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
# cuotas ordinarias. Realice un algoritmo que teniendo como dato de
# entrada el monto del préstamo, determine el monto total a pagar por
# el préstamo, el monto de las cuotas especiales y el monto de las
# cuotas ordinarias.
# =============================================================================
monto_prestamo = int(input('Ingrese monto del prestamo: ')) 
monto_total = (monto_prestamo * 0.24) + monto_prestamo 
cuota_especial = int(monto_total / 4)
cuota_ordinaria = int(monto_total / 20)
print('Monto total a pagar + intereses: ',monto_total)
print('Couta especial: ',cuota_especial)
print('Couta ordinaria: ',cuota_ordinaria)

# fin de este bloque
