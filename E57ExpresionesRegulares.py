# Las Expresiones Regulares son una secuencia de caracteres que forman un patron de busqueda
import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

# Metodo search() busca texto en una cadena de caracteres # Devuelve un objeto o none si no encuentra nada 

#print(re.search("aprender",cadena))

textoBuscar="aprender"

if re.search(textoBuscar, cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")

# Metodo start() nos dice el caracter donde comienza el texto encontrado
# Almacenamos el texto en una variable
textoEncontrado=re.search(textoBuscar, cadena)

print(textoEncontrado.start())

# Metodo start() nos dice el caracter donde finaliza el texto encontrado
print(textoEncontrado.end())

# Metodo span() nos dice el comienzo y el final
print(textoEncontrado.span())

# Vamos a buscar Python que aparece varias veces en el texto
# Metodo findall
textoBuscar="Python"
print(re.findall(textoBuscar, cadena))

print(len(re.findall(textoBuscar, cadena))) # Al agregarle len() nos dice el numero de veces que encuentra el texto


