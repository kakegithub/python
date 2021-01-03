# Programa que calcula la raiz cuadrada de un numero

import math # importamos la clase math

print("Programa de calculo de raiz cuadrada")
numero = int(input("Introduce un numero: "))

intentos=0 # variable para controlar el numero de intentos

while numero < 0: # comprobamos que no introduce un numero negativo
    print("No se puede hallar la raiz de un numero negativo")
    if (intentos == 2): # Le dejamos en realidad tres intentos (0,1,2)
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break; # Sale del bucle while
    
    numero=int(input("Introduce un numero: "))
    if (numero < 0):
        intentos = intentos + 1 # Suma los intentos

# Estamos fuera del bucle while
if (intentos < 2):
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))



