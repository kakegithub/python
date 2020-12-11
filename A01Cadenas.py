
# Programa que devuelve un mensaje por pantalla
mensaje="Hola Mundo"
print(mensaje)

mensaje="Bienvenidos a Python"
print(mensaje)

# Cadenas
cadena1="Esto es un string"
cadena2='Esto tambien es un string'
cadena3='Hola amigo, "Python es mi lenguaje favorito"'
cadena4="El lenguaje 'Python' tiene una sintaxis amigable"

print(cadena1)
print(cadena2)
print(cadena3)
print(cadena4)

# Ponemos en mayusculas la primera letra de cada palabra
nombre = 'ada lovelace'
print(nombre.title())

# Cambio de mayusculas a minusculas en una cadena con metodos
print(nombre.lower())

# Cambio de minusculas a mayusculas en una cadena con metodos
print(nombre.upper())

# Combinando y concatenando cadenas
nombre="ada"
apellido="lovelace"
nombre_completo=nombre + " " + apellido
print(nombre_completo)

print("Hola, " + nombre_completo.title() + "!" )

mensaje = "Hola, " + nombre_completo.title() + "!" 
print(mensaje)

# Agregar espacios en blanco a cadenas con tabulaciones o líneas nuevas
print("Python")
print("\tPython") # tabulacion

# Para agregar una nueva línea en una cadena, use la combinación de caracteres \n:
print("Lenguajes:\nPython\nJava\nC")

# Combinando tabulaciones y saltos de linea
print("Lenguajes:\n\tPython\n\tJava\n\tC")

# Quitar espacios en blanco
"""Para asegurarse de que no exista ningún espacio en blanco
    en el extremo derecho de una cadena, utilice el método rstrip ()"""

lenguaje_favorito = 'Python '
print(lenguaje_favorito)

lenguaje_favorito.rstrip()
print(lenguaje_favorito)

# Para quitar el espacio en blanco de forma definitiva hay que asignarlo a la variable
lenguaje_favorito = 'Python '
lenguaje_favorito = lenguaje_favorito.rstrip()
print(lenguaje_favorito)

"""Para asegurarse de que no exista ningún espacio en blanco
    en el extremo izquierdo de una cadena, utilice el método lstrip ()"""

lenguaje_favorito = lenguaje_favorito.lstrip()

"""Para asegurarse de que no exista ningún espacio en blanco
    en ambos lados de una cadena, utilice el método strip ()"""

lenguaje_favorito = lenguaje_favorito.strip()

# Evitar errores de sintaxis con cadenas
mensaje= "Una de las fortalezas de Python's es su comunidad diversa"
#mensaje = 'Una de las fortalezas de Python's es su comunidad diversa' # Esto daria error


