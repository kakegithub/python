# Serializando objetos

import pickle


class Vehiculos():
    
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enMarcha=True

    def acelerar(self): 
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enMarcha, "\nAcelera:", self.acelera,
            "\nFrena:", self.frena)


# Creamos tres objetos de la clase Vehiculos
coche1=Vehiculos("Mazda", "MX5")
coche2=Vehiculos("Seat", "Leon")
coche3=Vehiculos("Renault", "Laguna")

# Los almacenamos en una lista
coches=[coche1, coche2, coche3]

# Abrimos un fichero
fichero = open("LosCoches", "wb")

#Volacamos el contenido de la lista
pickle.dump(coches, fichero)

# Cerramos el fichero
fichero.close()

# Borramos el fichero de la memoria
del(fichero)

# Leemos el fichero
#fichero_apertura = open("LosCoches", "rb")

#Creamos una variable para volcar la informacion del fichero
#misCoches = pickle.load(fichero_apertura)

# Cerramos el fichero
#fichero_apertura.close()

# Leemos la informacion
#for c in misCoches:
#    print(c.estado())


