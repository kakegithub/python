# Rangos
import re

lista_palabras=['Ana',
                'Pedro',
                'María',
                'Rosa',
                'Sandra',
                'Celia'
                ]

print("--------------minusculas-------------")
for elemento in lista_palabras:
    # [] muestrame los elementos que hay entre la letra o y la letra t
    if re.findall('[o-t]', elemento):
            print(elemento)

print("--------------MAYUSCULAS-------------")
for elemento in lista_palabras:
    # [] muestrame los elementos que empiezen por la letra O o por la letra T
    if re.findall('^[O-T]', elemento):
        print(elemento)

print("--------------------------------------")
for elemento in lista_palabras:
    # [] muestrame los elementos que terminen por una letra comprendida entre la letra o la letra t
    if re.findall('[o-t]$', elemento):
        print(elemento)


lista_ciudades=['Ma.1',
                'Se1',
                'Ma2',
                'Ba1',
                'Ma:3',
                'Val1',
                'Val2',
                'Ma4',
                'MaA',
                'Ma.5',
                'MaB',
                'Ma:C'
            ]

print("----------PEDIDOS1-----------------------")
for elemento in lista_ciudades:
    # Muestrame los pedidos comprendidos entre el 0 y el 3
    if re.findall('Ma[0-3]', elemento):
        print(elemento)

print("----------PEDIDOS2-----------------------")
for elemento in lista_ciudades:
    # Muestrame los pedidos comprendidos que no esten entre el 0 y el 3
    if re.findall('Ma[^0-3]', elemento):
        print(elemento)

print("----------PEDIDOS3-----------------------")
for elemento in lista_ciudades:
    # Muestrame los pedidos comprendidos que esten entre el 0 y el 3, y la A y la B
    if re.findall('Ma[0-3A-B]', elemento):
        print(elemento)

print("----------PEDIDOS4-----------------------")
for elemento in lista_ciudades:
    # Muestrame los pedidos cuyo tercer caracter sea un punto o dos puntos
    if re.findall('Ma[.:]', elemento):
        print(elemento)
