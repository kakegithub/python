# Recorrer una lista completa
magos = ["Alicia", "David", "Carolina"]
for mago in magos:
    print(mago)
    print(mago.title() + " hizo un gran truco")

print("Gracias, ha sido un bonito espectaculo")

# Listas numericas. Funcion range()
for valor in range(1, 5):
    print(valor)

# Usando range() para crear una lista numerica
numeros = list(range(1, 6))
print(numeros)

# Otro uso de range.
# Creamos una lista que empiece por el numero 2 que contenga los elementos comprendidos hasta el 11 de dos en dos.
numeros2 = list(range(2,11,2))
print(numeros2)

# Otro ejemplo. Recorremos un rango del 1 al 11. Elevados el valor a dos y lo añadimos a la lista vacia potencias.
potencias = []
for valor in range(1,11):
    potencia = valor ** 2
    potencias.append(potencia)
print(potencias)

# Optimizando el codigo
potencias = []
for valor in range(1,11):
    potencias.append(valor ** 2)
print(potencias)

# Optimizando el codigo
potencias = [valor ** 2 for valor in range(1,11)]
print(potencias)


# Estadisticas en una lista numerica
digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digitos))
print(max(digitos))
print(sum(digitos))

# Extraer un rango de la lista
jugadores = ['Carlos', 'Martina', 'Mike', 'Aurelio', 'Eli']
print(jugadores[0:3])
print(jugadores[1:4])
print(jugadores[:4])
print(jugadores[2:])
print(jugadores[-3:])

print("Estos son los tres primeros jugadores")
for jugador in jugadores[:3]:
    print(jugador.title())

# Copiando una lista
comidas = ['Pizza', 'Macarrones', 'Arroz']
misComidas = comidas[:]

print("Lista comidas:")
print(comidas)
print("Lista misComidas: ")
print(misComidas)

comidas.append("Canelonis")
misComidas.append("Helado")

print("Lista comidas:")
print(comidas)
print("Lista misComidas: ")
print(misComidas)







 

