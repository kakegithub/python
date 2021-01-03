
class Perro():
    """ Una clase que define a un perro """

    def __init__(self, nombre, edad):
        #super().__init__()
        """ Definimos atributos nombre y edad """
        self.nombre = nombre
        self.edad = edad

    def sentarse(self):
        """ Metodo que simula que el perro se sienta """
        print(self.nombre.title() + " esta sentado")

    def volverse(self):
        """ Metodo que simula que el perro se da la vuelta """
        print(self.nombre.title() + " se ha dado la vuelta")

    
# Creando instancias de la clase
mi_perro = Perro("Brenda", 6)
tu_perro = Perro("Coco", 12)

print("Mi perro se llama " + mi_perro.nombre.title())
print("Mi perro tiene " + str(mi_perro.edad) + " años")

# LLamando a los metodos
mi_perro.sentarse()
mi_perro.volverse()

tu_perro.sentarse()
tu_perro.volverse()





















