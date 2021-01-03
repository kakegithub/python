# Instrucciones continue - pass - else
# continue---------> Salta a la siguiente iteracion de bucle
# pass-------------> devuelve null
# else-------------> tiene el mismo sentido de un condicional

# Ejemplo continue
for letra in "python":
    
    if (letra == "h"):
        continue # Hace que se salte la iteracion de la letra "h"
    print("Viendo la letra: " + letra)

# Ejemplo continue
nombre = "pildoras informaticas"

contador = 0

for i in nombre:
    
    if i == " ":
        continue # Salta la iteracion cuendo encuentra un espacio en blanco y no aumenta el contador
    
    contador+=1

print(nombre)
print(contador) # Da 20 caracteres

#print(len(nombre)) # Cuenta el espacio en blanco por eso nos da 21 caracteres

# Ejemplo pass
#while True:
    #pass # Se mantiene hasta que pulsamos ctrl + c

# Ejemplo pass
class MiClase: # Esto es una clase nula
    pass # Para implementar mas tarde

# Ejemplo else
email = input("Introduce su email: ")

for i in email: # recorremos el email
    if i == "@":
        arroba = True
        break; # Si encuentra la arroba sale del bucle

else: # Se ejecuta cuando el bucle ha terminado
    arroba = False

print(arroba)







