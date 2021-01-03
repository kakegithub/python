# Leyendo un archivo de texto.txt
with open('pi_digitos.txt') as file_object:
    contenido = file_object.read()
    print(contenido)
    #print(contenido.rstrip()) # Remueve los espacios en blanco

# Leyendo de otra carpeta un archivo de texto.txt
with open('archivos_texto/fichero.txt') as file_object:
    contenido = file_object.read()
    print(contenido)

# Leyendo linea a linea
archivo = 'archivos_texto/fichero.txt'
with open(archivo) as file_object:
    for linea in file_object:
        print(linea)

# Haciendo una lista de lineas de la fila
archivo = 'pi_digitos.txt'
with open(archivo) as file_object:
    lineas = file_object.readlines()

for linea in lineas:
    print(linea.rstrip())

# Escribiendo una linea vacia
archivo = 'programando.txt'
with open(archivo, 'w') as file_object:
    file_object.write("Me gusta programar")

# Añadiendo linea al fichero
archivo = 'programando.txt'
with open(archivo, 'a') as file_object:
    file_object.write("Otra linea añadida al fichero")



