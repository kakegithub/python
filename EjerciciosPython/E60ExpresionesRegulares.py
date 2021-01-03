# Modulo re
# Funciones Math y search

import re

nombre1="Sandra Lopez"
nombre2="Antonio Lopez"
nombre3="sandra Lopez"
nombre4="Jara Lopez"
nombre5="Sara Lopez"
# Funcion Math() busca coincidencias en un patron de busqueda al comienzo de una cadena de texto

if re.match("Sandra", nombre1):
    print("Hemos encontrado el nombre " + nombre1)
else:
    print("No hemos encontrado el nombre ")


if re.match("Sandra", nombre2):
    print("Hemos encontrado el nombre " + nombre2)
else:
    print("No hemos encontrado el nombre ")

if re.match("Sandra", nombre3, re.IGNORECASE):
    print("Hemos encontrado el nombre " + nombre3)
else:
    print("No hemos encontrado el nombre " )

if re.match(".ara", nombre4, re.IGNORECASE):
    print("Hemos encontrado el nombre " + nombre4)
else:
    print("No hemos encontrado el nombre ")


if re.search("Lopez", nombre4, re.IGNORECASE):
    print("Hemos encontrado el nombre " + nombre4)
else:
    print("No hemos encontrado el nombre ")


print("---------------------------------------------")
cadena1 = "Jara Lopez"
cadena2 = "5465465456"
cadena3 = "a54654654"

# \d busca si hay un digito al principio de la cadena con math()
if re.match("\d", cadena1):
    print("Hemos encontrado el numero ")
else:
    print("No hemos encontrado el numero ")

# \d busca si hay un digito en toda la cadena con search()
if re.match("\d", cadena2):
    print("Hemos encontrado el numero ")
else:
    print("No hemos encontrado el numero ")

 
codigo1 ="dñlaskdasñlkasdñlk´kada71ñlak´dkañsljda´sñjd"
codigo2 = "yiuqwyiu71hdljhaskjhasdkahdsk kkd kks"
codigo3 = "ñkdñlkadsñkañlskañslkdñlskadñsañadskañska"

# Devuelve TRUE o FALSE
print("-------------searh---------------")
if re.search("71", codigo1):
    print("Hemos encontrado el numero")
else:
    print("No hemos encontrado el numero")

