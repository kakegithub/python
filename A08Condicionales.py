# Condicionales
coches = ["audi", "bmw", "subaru", "toyota"]
for coche in coches:
    if coche == "bmw":
        print(coche.upper())
    else:
        print(coche.title())

# La prueba de igualdad distingue entre mayúsculas y minúsculas en Python.
# Dependiendo del caso podemos convertir el valor de la variable a minusculas para comparar.

car = "Audi"
car.lower() == "audi"

# Comparador de desigualdad
respuesta = "hongos"
if respuesta != "anchoas":
    print("Quiero anchoas")

# Comparaciones numericas
numero = input("Introduce un numero:")
if int(numero) != 42:
    print("Numero incorrecto")

edad1 = 14
edad2 = 21

# Operador de comparacion AND
if ((edad1 >= 18) and (edad2 >= 18)):
    print("Los dos sois mayores de edad")

# Operador de comparacion OR
if ((edad1 < 18) or (edad2 < 18)):
    print("Hay un menor de edad entre vosotros")

# Comprobar si un valor esta en una lista
colores = ["rojo", "azul", "verde"]
comprobacion = "rojo" in colores
print(comprobacion)

# Comprobar que un valor no esta en una lista
nombres = ["Ana", "Juan", "Patricia"]
nombre = input("Introduce tu nombre:")
if nombre not in nombres:
    print(nombre.title() + " no esta en la lista")
else:
    print("El nombre de usuario " + nombre + " ya existe")

# Expresiones Booleanas
juego_activo = True
puede_editar = False

if juego_activo:
    puede_editar = True

edad = input("Introduce tu edad:")
if int(edad) < 4:
    print("Coste maticula 0€")
elif int(edad) < 18:
    print("Coste maticula 8€")
else:
    print("Coste maticula 12€")

# Usando condicionales con listas
frutas = ["manzana", "pera", "kiwi", "platano"]
for fruta in frutas:
    if(fruta == "platano"):
        print("Lo siento no tenemos platanos")
    else:
        print("Tenemos de postre " + fruta.title())


# Usando multiples listas
ingredientes_disponibles = ['tomate', 'olivas', 'pepinillos','pepperoni', 'piña', 'extra de queso']
ingredientes_pedidos = ['tomate', 'patatas fritas', 'extra de queso']
for ingrediente_pedido in ingredientes_pedidos:
    if ingrediente_pedido in ingredientes_disponibles:
        print("Añadiendo " + ingrediente_pedido + ".")
    else:
        print("Lo siento, no tenemos " + ingrediente_pedido + ".")
        
print("\nTu pizza esta preparada!")