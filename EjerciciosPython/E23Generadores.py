# Instruccion yield from
# Sirve para simplificar el codigo del generador en el caso de utilizar bucles anidados

def devuelve_ciudades(*ciudades): # El * significa que no sabemos cuentos argumentos le vamos a pasar y los devuelve en forma de tupla
    for elemento in ciudades: # Recorremos los argumentos
        for subElemento in elemento: # Recorremos los subelementos
            yield subElemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print("Con yield from seria")
def devuelveCiudades(*ciudades): # El * significa que no sabemos cuentos argumentos le vamos a pasar y los devuelve en forma de tupla
        for elemento in ciudades: # Recorremos los elementos
            yield from elemento # devuelve el subelemento

ciudadesDevueltas = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudadesDevueltas))

print(next(ciudadesDevueltas))
