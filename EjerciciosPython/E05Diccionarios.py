# Diccionarios en Python

# Son estructuras de datos que nos permiten almacenar valores de diferente tipo(entero, cadena de texto, decimales)
# e incluso listas y otros diccionarios.

# Los datos se almacenan asociados a una clave-----------> clave:valor

# Los elementos almacenados no estan ordenados.

# Sintasis de un diccionario

miDiccionario = {"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}

print(miDiccionario["Francia"]) # Paris

# Acceder al diccionario completo
print(miDiccionario)

# Agregar elementos a un diccionario
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

# Modificar un valor del diccionario
miDiccionario["Italia"]="Roma" # Sobreescribimos  
print(miDiccionario)

# Eliminar un elemento. Metodo del()
del miDiccionario["Reino Unido"]
print(miDiccionario)

# Diccionario con valores de distinto tipo
miDiccionario2={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(miDiccionario2)

# Utilizar una tupla para asignar las claves a cada uno de los valores
miTupla=["España", "Francia", "Reino Unido", "Alemania"]
miDiccionario3={miTupla[0]:"Madrid",miTupla[1]:"Paris",miTupla[2]:"Londres",miTupla[3]:"Berlin"}
print(miDiccionario3)

# Accediendo a los elementos
print(miDiccionario3["Francia"])
print(miDiccionario3[miTupla[0]])

# Diccionario que almacene una tupla
miDiccionario4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "anillos":[1991, 1992, 1993, 1996,1997, 1998]}
print(miDiccionario4)

print(miDiccionario4["Equipo"])

print(miDiccionario4["anillos"])

# Guardar diccionario en otro diccionario
miDiccionario5={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "anillos":{"temporadas":[1991, 1992, 1993, 1996,1997, 1998]}}
print(miDiccionario5)

# Nos devuelve las claves de un diccionario
print(miDiccionario4.keys())

# Nos devuelve los valores
print(miDiccionario5.values())