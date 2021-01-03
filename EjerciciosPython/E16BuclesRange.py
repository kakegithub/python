# Uso de range()

for i in range(5): # Desde el valor 0 hasta el 4 (0,1,2,3,4)
    print (f"valor de la variable {i}") # Concatena un texto con el valor que va tomando i

for i in range(5,10): # Desde el valor 5 hasta el 9 (5,6,7,8,9)
    print (f"valor {i}") # Concatena un texto con el valor que va tomando i

for i in range(5,50,3): # Desde el valor 5 hasta el 49 saltando de 3 en 3 (5,8,11,14,.....47)
    print (f"salto {i}") # Concatena un texto con el valor que va tomando i

# Funcion len()-------> Devuelve la longitud de un String
print(len("Juan")) # 4


# Comprobar Email. Hay que perfeccionarlo
valido = False

email = input("Introduce tu email")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("Email correcto")
else:
    print("Email invalido")


