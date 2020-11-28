#Serializacion
# Biblioteca pickle

import pickle 
lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario=open("lista_nombres", "wb") # Lo abrimos como escritura binaria

# Volcado de la lista al fichero. Metodo dump()
pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close() # Cerramos el fichero
del(fichero_binario) # Borramos de la memoria

# Accedemos a la informacion
fichero_binario=open("lista_nombres", "rb")
lista=pickle.load(fichero_binario) # volamos la informacion a lista
print(lista)







