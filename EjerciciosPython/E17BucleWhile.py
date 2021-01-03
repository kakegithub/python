# Bucle Indeterminado
# Sintaxis Bucle while
# While condicion:

i = 1

while i <= 10:
    print("Ejecucion:" + str(i))
    i = i + 1
print("Termino la ejecucion")


# Ejemplo bucle indeterminado
edad = int(input("Introduce la edad: "))

while edad < 0:
    print("Has introducido una edad negativa. Vuelve a intentarlo")
    edad = int(input("Introduce la edad: "))

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante: " + str(edad))