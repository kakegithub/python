import pickle

# Leemos el fichero
fichero_apertura = open("LosCoches", "rb")

#Creamos una variable para volcar la informacion del fichero
misCoches = pickle.load(fichero_apertura)

# Cerramos el fichero
fichero_apertura.close()

# Leemos la informacion
for c in misCoches:
    print(c.estado())

