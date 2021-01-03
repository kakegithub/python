
class Coche():
    """ Una clase que representa a un coche """

    def __init__(self, marca, modelo, anio):
        #super().__init__()
        """ Atributos que definen a un coche """
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.km = 0

    def descripcion(self):
        """ Devuelve una descripcion del coche """
        detalles = str(self.anio) + " " + self.marca + " " + self.modelo
        return detalles.title()

    def cuentakm(self):
        """ Lee el cuentakm """
        kilometros = self.km
        return "Este coche ha hecho " + str(kilometros) + " km"


    # Modificando el valor de un atributo a trves de un metodo
    def modificar_cuentakm(self, kmof):
        if kmof > self.km:
            self.km = kmof
        else:
            print("No puedes quitarle km al cuentakm")


mi_nuevo_coche = Coche("Audi", "A4", 2020)
datos = mi_nuevo_coche.descripcion()
print(datos)

kilometros = mi_nuevo_coche.cuentakm()
print(kilometros)

# Modificando el valor de un atributo directamente
mi_nuevo_coche.km = 23



mi_nuevo_coche.modificar_cuentakm(35)
print(mi_nuevo_coche.cuentakm())


mi_nuevo_coche.modificar_cuentakm(15)
print(mi_nuevo_coche.cuentakm())


