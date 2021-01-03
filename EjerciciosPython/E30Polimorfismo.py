# Polimorfismo. Un objeto puede cambiar de forma y comportamiento

class Coche():

    def desplazamiento(self):
        print("Me desplazo usando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo usando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo usando 6 ruedas")
 
# Una forma de hacerlo
#miVehiculo=Moto()
#miVehiculo.desplazamiento()

#miVehiculo2=Coche()
#miVehiculo2.desplazamiento()

#miVehiculo3=Camion()
#miVehiculo3.desplazamiento()

# Usando Polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Camion()
desplazamientoVehiculo(miVehiculo) # LLama al metodo de la clase Camion

miVehiculo2=Coche()
desplazamientoVehiculo(miVehiculo2) # LLama al metodo de la clase Coche


