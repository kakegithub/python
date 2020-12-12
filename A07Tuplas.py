# Tuplas

dimensiones = (200, 50)
print(dimensiones[0])
print(dimensiones[1])

# Recorriendo los valores de una tupla
print("--------Recorriendo Valores----------")
for dimension in dimensiones:
    print(dimension)

# Sobreescribir una tupla
print("Dimensiones Originales:")
for dimension in dimensiones:
    print(dimension)

print("Dimensiones Modificadas:")
dimensiones = (400, 100)
for dimension in dimensiones:
    print(dimension)
