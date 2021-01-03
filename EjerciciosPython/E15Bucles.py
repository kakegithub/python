# Bucle for

for i in ["pildoras", "informaticas", 3]:
    print("Hola", end=" ") # pone Hola una al lado de otra con un espacio


for i in ["pildoras", "informaticas", 3]:
    print("Hola", end="       ") # Con mas espacios

# Recorriendo Strings
# Comprobando un email. Falta perfeccionarlo

contador = 0
miEmail = input("Introduce tu direccion de email:")
for i in miEmail: 
    if(i=="@" or i == "."):
        contador = contador + 1
if contador == 2:
    print("Email correcto")
else:
    print("Email incorrecto")

