# Organizacion de Listas
# El método sort() de Python hace que sea relativamente fácil ordenar una lista
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("Ordenando la lista en orden alfabetico")
cars.sort()
print(cars)

# Ordenar la lista en orden alfabetico inverso
print("Ordenando la lista en orden alfabetico inverso")
cars.sort(reverse=True)
print(cars)
print("\n")

# Ordenar una lista temporalmente con la función sorted()
# La función sorted() le permite mostrar su lista en un orden en particular, pero no afecta el orden real de la lista.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Lista Original:")
print(cars)
print("\nOrdenada temporalmente:")
print(sorted(cars))
print("\nLista Original:")
print(cars)

# Imprimiendo una lista en orden inverso
print("Lista en orden inverso")
cars.reverse()
print(cars)

# Encontrar la longitud de una lista metodo len()
print(len(cars)) # tiene 4 elementos



