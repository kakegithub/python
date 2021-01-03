
# Archivos
from io import open

archivo_texto = open("archivo.txt","w") # Abrimos el archivo en modo escritura si no existe lo crea
frase = "Estupendo dia para aprender python \n el sabado"
archivo_texto.write(frase) # Escribimos en el archivo
archivo_texto.close() # Cerramos el archivo

archivo_texto = open("archivo.txt","r") # Abrimos el archivo en modo lectura
texto = archivo_texto.read()
archivo_texto.close()
print(texto)

archivo_texto = open("archivo.txt","r")
lineas_texto = archivo_texto.readlines() # Guarda la informacion en una lista
archivo_texto.close()
print(lineas_texto)

archivo_texto = open("archivo.txt","a") # Abrimos archivo para añadir
archivo_texto.write("\n siempre es una buena ocasion para estudiar python")
archivo_texto.close()

# Uso de punteros
archivo_texto = open("archivo.txt","r") # Abrimos el archivo en modo lectura
print(archivo_texto.read())
print("--------------------------------------")
# Modificamos la posicion del puntero o cursor
archivo_texto.seek(0) # Se pone en la posicion 0
print(archivo_texto.read())
print("--------------------------------------")

archivo_texto.seek(11) # Se pone en la posicion 11
print(archivo_texto.read())
print("--------------------------------------")

archivo_texto.seek(0) # Se pone en la posicion 0
print(archivo_texto.read(11)) # Lee el archivo hasta la posicion 11
print("--------------------------------------")

archivo_texto.seek(len(archivo_texto.read())/2) # pone el cursor en la mitad del archivo
print(archivo_texto.read())
archivo_texto.close()
print("--------------------------------------")

archivo_texto = open("archivo.txt","r+") # Abrimos el archivo en modo lectura y escritura
#print(archivo_texto.readlines())

lista_texto = archivo_texto.readlines()
lista_texto[2]=" Esta linea ha sido incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()
print("----------------------------------------")