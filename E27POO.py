# POO (Programacion orientada a objetos)

class Coche():

    #Constructor de la clase
    def __init__(self):
        # Propiedades
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4 #Encapsulamos esta propiedad para que no se pueda modificar desde el exterior de la clase
        self.__enMarcha=False

    # Comportamiento(metodos)
    def arrancar(self,arrancamos): # self hace referencia al propio objeto, instancia o ejemplar de la clase
        self.__enMarcha=arrancamos # Le pasamos la variable del metodo

        if (self.__enMarcha):
            chequeo = self.__chequeoInterno()
        if (self.__enMarcha and self.chequeo): # Si es igual a TRUE
            return "Mi coche esta en marcha"
        elif (self.__enMarcha and self.chequeo==False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            return "Mi coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas", " un ancho de ", self.__anchoChasis, " cm", " y un largo de ",
                self.__largoChasis, " cm")


    def __chequeoInterno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

# instancia de clase
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()


print("---------------- A continuacion creamos el segundo objeto -----------------")
miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()


