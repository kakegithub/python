# Listas en python
# nombreLista = [elemento1, elemento2, elemento3, ....]

# Las listas en python pueden almacenar distintos tipos de datos

# Las listas empiezan a contar desde el elemento con indice 0 en este caso "Maria" 
miLista = ["Maria", "Pepe", 78.35, "Marta", "Antonio", "Maria", 8, True] # Creando una lista

print(miLista[:]) # Imprimiendo la lista

print(miLista[0]) # Imprimiendo el primer elemento de la lista


print(miLista[-1])# Si empezamos por el final empieza a contar desde -1 en este caso "Antonio"

# Porcion de Lista. Util cuando las listas son largas
print (miLista[1:3]) # Imprime el indice 1 y 2.

# Nomenblatura abreviada
print(miLista[:3]) # Accedemos a los tres primeros elementos. "Maria" "Pepe" "Marta"
print(miLista[1:]) # Accede desde el elemto 1 hasta el final. "Pepe" "Marta" "Antonio"

# Agregar elementos a una lista. Funcion append(). append() agrega el elemento al final de la lista
miLista.append("Sandra")

print(miLista[:])

# Agregar un elemento a la lista en una posicion. Funcion insert()
miLista.insert(2,"Carlos")

print(miLista[:])

# Agregar varios elementos a la lista. Funcion extend(). Es como si concatenasemos otra lista
miLista.extend(["Jordan","Erika"])
print(miLista[:])

# Funcion que nos devuelve el indice de un elemento dentro de una lista. Funcion index()
print(miLista.index("Carlos"))

# Comprobar que un elemento se encuentra o no en una lista.
print("Pepe" in miLista) # devuelve TRUE. "Pepe" esta en la lista
print("Jolumo" in miLista) # devuelve FALSE. "Jolumo" no esta en la lista

# Eliminar elementos en una lista. Funcion remove()
print(miLista[:])
miLista.remove("Maria") # Eliminamos a "Maria 
miLista.remove(78.35) # Eliminamos el 78.35
print(miLista[:])

# Eliminar el ultimo elemento de la lista. Funcion pop()
miLista.pop()
print(miLista[:])

# Sumar listas. Lo que hace es unir las listas
miLista2=["Koke", "Yoli"] # Creamos una lista

print(miLista2[:])

miLista3=miLista + miLista2 # Sumamos las listas

print(miLista3[:])

# Repetir listas.
print("Repitiendo lista")
miLista4=[1,2,3,4] * 3
print(miLista4[:])

