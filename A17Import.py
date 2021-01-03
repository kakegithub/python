
from collections import OrderedDict
lenguajes_favoritos = OrderedDict()

lenguajes_favoritos['Carlos']='Java'
lenguajes_favoritos['Pedro']='Python'
lenguajes_favoritos['Erika']='C++'
lenguajes_favoritos['Ana']='Ruby'

for nombre, lenguaje in lenguajes_favoritos.items():
    print("El lenguaje de programacion favorito de " + nombre.title() + " es " + lenguaje.title())




