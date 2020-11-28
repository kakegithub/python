# Operadores logicos 
# AND ---------> y si   
# OR-----------> o si no
# Operador IN -----------> 

# Programa que evalua si un alumno tiene derecho a beca si cumple distancia > 40 y numeroHermanos > 2 o que 
# salarioFamiliar <= 20000 aunque no cumpla las dos condiciones anteriores    

distanciaEscuela = int(input("Introduce la distancia en km: "))
print(distanciaEscuela)
numeroHermanos = int(input("Introduce el numero de hermanos: "))
print(numeroHermanos)
salarioFamiliar = int(input("Introduce salario familiar bruto: "))
print(salarioFamiliar)

if distanciaEscuela > 40 and numeroHermanos > 2 or salarioFamiliar <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")
