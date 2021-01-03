# Guardadr datos de forma permanente en ficheros

import pickle
class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self): # Convierte en cadena de texto la informacion de un objeto
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    
    personas=[] #Creamos una lista donde almacenar a las personas

    # Creamos un constructor
    def __init__(self):
        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0) # Desplazamos el cursor al inicio

        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self,p):
         self.personas.append(p)
    
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasFicheroExterno(self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero es la siguiente:")
        for p in self.personas:
            print(p)



# Creamos un objeto ListaPersonas
miLista = ListaPersonas()
# Creamos una persona
persona = Persona("Sandra", "Femenino", 29)
# La añadimos a la lista
miLista.agregarPersonas(persona)

# Creamos una persona
persona = Persona("Carlos", "Masculino", 34)
# La añadimos a la lista
miLista.agregarPersonas(persona)

# Creamos una persona
persona = Persona("Erika", "Femenino", 21)
# La añadimos a la lista
miLista.agregarPersonas(persona)

# Mostramos las personas
miLista.mostrarPersonas()

miLista.mostrarInfoFicheroExterno()
