# Tuplas en Python
# Las Tuplas no se pueden modificar una vez creadas
# No permiten añadir, eliminar, mover elementos, etc (no append, extend, remove)
# Si Permiten extraer porciones pero el resultado es una tupla nueva
# Se permiten busquedas (index)
# Si permiten comprobar si un elemento se encuentra en la tupla

# Utilidad respecto a las listas
    # Mas rapidas
    # Menos espacio(Mayor optimizacion)
    # Formatean Strings
    # Pueden utilizarse como claves en un diccionario(Las listas no)

# Sintasis de una Tupla
# nombreTupla = (elemento1, elemento2, elemento3,...)

miTupla=("Juan", 13, 1, 1995, 13) # Creamos una tupla

print(miTupla[1]) # Accedemos al elemento 1 de la tupla

# Convertir tupla en lista. Metodo list()
miLista = list(miTupla) 
print(miLista)

# Convertir lista en tupla. Metodo tuple()
miTupla = tuple(miLista)
print(miTupla)

# Comprobar si hay elementos en la tupla. Instruccion in
print("Juan" in miTupla) # Da TRUE. "Juan" si esta en la tupla

# Saber cuantos elementos del que preguntamos hay dentro de una tupla . Metodo count()
print(miTupla.count(13)) # Cuantos 13 hay en la tupla # Hay un 13

# Calcular longitud de la tupla. Metodo len()
print(len(miTupla))
print(miTupla.__len__())

# Tupla de 1 elemento. Ojo a la ,
miTupla2=("Oscar",)
print(len(miTupla2))

# Desempaquetado de tupla
print("Desempaquetado de tuplas")
miTupla=("Juan",13,1,1995)

nombre, dia, mes, agno=miTupla # Asignamos los valores de la tupla a estas variables por orden

print(nombre)
print(dia)
print(mes)
print(agno)





