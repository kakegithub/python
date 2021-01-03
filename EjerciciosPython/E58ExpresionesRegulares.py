# Metacaracteres(caracteres comodin)

import re
lista_nombres=['Ana Gomez',
                'Maria Martin', 
                'Sandra Lopez', 
                'Santiago Martin',
                'Sandra Fernandez']

lista_web=['http://mipagina.es',
            'ftp://mipagina.es',
            'http://mipagina.com',
            'ftp://mipagina.com', 
            'informaticaenespaña.es'
            ]
lista_palabras=['hombres',
                'mujeres',
                'mascotas',
                'camión',
                'camion',
                'niños',
                'niñas'
                ]




for elemento in lista_nombres:
    # ^ que empieza por
    if re.findall('^Sandra', elemento):
        print(elemento)


for elemento in lista_nombres:
    # $ que finaliza por
    if re.findall('Martin$', elemento):
        print(elemento)

for elemento in lista_web:
    # $ que finaliza por
    if re.findall('es$', elemento):
        print(elemento)

for elemento in lista_web:
    # ^ que empieza por
    if re.findall('^ftp', elemento):
        print(elemento)
 
for elemento in lista_web:
    # [] que tenga lo que hay entre los corchetes
    if re.findall('[ñ]', elemento):
        print(elemento)


for elemento in lista_palabras:
    # [] que tenga lo que hay entre los corchetes
    if re.findall('niñ[oa]s', elemento):
        print(elemento)

for elemento in lista_palabras:
    # [] que tenga lo que hay entre los corchetes
    if re.findall('cami[óo]n', elemento):
        print(elemento)
