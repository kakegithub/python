from A12Funciones import hacer_pizza
# Importando el modulo
import modulopizza
# Importando funciones especificas
from modulopizza import hacer_pizza
# Poniendo un alias a la funcion
from modulopizza import hacer_pizza as hz
# Importando todas las funciones de un modulo
from modulopizza import *

hacer_pizza('pequeño','mozarella','tomate')
hz('grande','queso','setas','romero')

