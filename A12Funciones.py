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
def obtener_musico(nombre, apellido):
    nombre_completo = {"Nombre:":nombre, "Apellido:":apellido}
    return nombre_completo

musico = obtener_musico("alejandro", "sanz")
print(musico)



