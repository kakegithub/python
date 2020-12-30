# Introducción a las funciones
def saludo_usuario():
    print("Hola")

saludo_usuario()

# Paso de parametros
def saludo(nombre):
    print("Hola " + nombre.title())

saludo("Pepe")

def describe_mascota(tipo,nombre):
    print("\nTengo un " + tipo + ".")
    print("\nSe llama " + nombre.title() + ".")

describe_mascota("gato", "riau")
describe_mascota(tipo="perro", nombre="Brenda")

# Devolviendo valores
def obtener_musico(nombre, apellido):
    nombre_completo = nombre + " " + apellido
    return nombre_completo.title()

musico = obtener_musico("alejandro", "sanz")
print(musico)

# Devolviendo un diccionario
def obtener_musico(nombre, apellido, edad = ""):
    nombre_completo = {"Nombre:":nombre, "Apellido:":apellido}
    if edad:
        nombre_completo['edad']=edad
    return nombre_completo
musico = obtener_musico("alejandro", "sanz", 54)
print(musico)


# Funcion con bucle
def obtener_nombre_completo(nombre, apellido):
    """Devuelve el nombre completo formateado."""
    nombre_completo = nombre + ' ' + apellido
    return nombre_completo.title()

while True:
    print("\nDime tu nombre:")
    print("(Introduce 'q' para salir)")
    
    nombre = input("Nombre: ")
    if nombre == 'q':
        break
    
    apellido = input("Apellido: ")
    if apellido == 'q':
        break
    nombre_formateado = obtener_nombre_completo(nombre, apellido)
    print("\nHola, " + nombre_formateado + "!")

# Pasando una lista a la funcion
def saludo_users(nombres):
    # Imprime un saludo para cada miembro de la lista
    for nombre in nombres:
        msg = "Hola " + nombre.title() + "!"
        print(msg)

usuarios = ["Lola", "Carla", "Luis"]
saludo_users(usuarios)

# Modificando una lista en una funcion
disegno_inicial = ['Iphone', 'Motorola', 'Xiaomi']
disegno_final = []

while disegno_inicial:
    disegno_actual = disegno_inicial.pop()
    print("Imprimiendo modelo: " + disegno_actual)
    disegno_final.append(disegno_actual)

print("Modelos finales:")
for disegno in disegno_final:
    print(disegno)

# Pasando un numero indeterminado de argumentos
def hacer_pizza(tamano, *ingredientes):
    print("Ingredientes de la pizza " + str(tamano))
    for ingrediente in ingredientes:
        print("-" + ingrediente)

hacer_pizza('Mediana','mozarella', 'tomate', 'champichon', 'Setas')

hacer_pizza('Pequeña','mozarella', 'tomate', 'York')

# Pasando tipos de argumentos distintos
def construir_perfil(nombre, apellido, **informacion): # El doble asterisco crea un diccionario llamado informacion
    perfil={}
    perfil["Nombre:"]=nombre
    perfil["Apellido:"]=apellido
    for llave,valor in  informacion.items():
        perfil[llave]=valor
    return perfil

perfil_usuario = construir_perfil('Pepe','Gotera',Localizacion='Cadiz',Oficio='chapuzas')
print(perfil_usuario)







