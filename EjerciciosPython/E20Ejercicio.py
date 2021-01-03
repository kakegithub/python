# Crea un programa que pida números positivos indefinidamente. El programa termina cuando se introduce un número negativo. 
# Finalmente el programa muestras la suma de todos los números introducidos

numero = int(input("Introduce un numero: "))


while(numero > 0):
    suma = suma + numero
    numero = int(input("Introduce un numero: "))

print("Suma: " + str(suma))