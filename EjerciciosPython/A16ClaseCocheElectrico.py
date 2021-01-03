# Herencia
from A15ClaseCoche import Coche

class CocheElectrico(Coche):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio)
        self.bateria = 70

    def descripcion_bateria(self):
        """ Describe el tamaño de la bateria """
        print("Este coche tiene una bateria de " + str(self.bateria) + " kw")

mi_tesla = CocheElectrico('Tesla', 'modelo s', '2021')
print(mi_tesla.descripcion())
mi_tesla.descripcion_bateria()
