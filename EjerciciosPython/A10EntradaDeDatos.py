# Entrada de Datos
from typing import SupportsIndex


#nombre = input("Introduce tu nombre:")
#print("Tu nombre es " + nombre + "!")

# Mensajes de mas de una linea
mensaje = "Me gustaria saber tu nombre."
mensaje += "\nComo te llamas:"
nombre = input(mensaje)
print("Tu nombre es " + nombre + "!")

# Usando int() para aceptar entradas numericas
edad = input("Que edad tienes:")
edad = int(edad)
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

    