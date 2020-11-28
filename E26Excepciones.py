
# raise permite personalizar el mensaje
def evaluaEdad(edad):
    if edad < 0: # Personalizamos la excepcion
        #raise TypeError("No se permiten edades negativas")
        raise miPropioError("No se permiten edades negativas")

    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate"
    
print(evaluaEdad(18))

import math
def calculaCuadrado(num):
    if num < 0:
        raise ValueError ("El numero no puede ser negativo")
    else:
        return math.sqrt(num)
    
op1 = int((input("Introduce un numero: ")))
try:
    print(calculaCuadrado(op1))
except ValueError as errorNumeroNegativo:
    print(errorNumeroNegativo)

print("Programa terminado")