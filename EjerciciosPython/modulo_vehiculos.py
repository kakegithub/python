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

#Clase Furgoneta hereda de la clase Vehiculos
class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"





# La clase Moto hereda de la clase Vehiculos
class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enMarcha, "\nAcelera:", self.acelera,
            "\nFrena:", self.frena, "\n", self.hcaballito)


class VElectricos(Vehiculos):
    
    def __init__(self, marca, modelo):
        
        super().__init__(marca, modelo)

        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando=True 

#Herencia multiple
class BiciletaElectrica(VElectricos, Vehiculos): # Le damos preferencia a VElectricos. constructor y metodos
    pass


