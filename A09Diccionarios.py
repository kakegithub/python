# Diccionarios
alien_0 = {'color':'verde', 'puntos':5 }
print(alien_0['color'])
print(alien_0['puntos'])

# Guardamos el valor puntos en una variable 
puntos_nuevos=alien_0['puntos']
print("Has conseguido " + str(puntos_nuevos) + " puntos")

# Añadiendo una nueva clave:valor al diccionario
alien_0['posicionx']=0
alien_0['posiciony']=25

print(alien_0)

# Modificando valores en un diccionario
print("El alien es de color " + alien_0['color'])
alien_0['color']='amarillo'
print(alien_0)
print("El alien es ahora de color " + alien_0['color'])

# Ejemplo
alien_1={'posicionx' : 0, 'posiciony' : 25, 'velocidad' : 'media'}
print("Original posicion x:" + str(alien_1['posicionx']))

if alien_1['velocidad'] == 'baja':
    incrementax = 1
elif alien_1['velocidad'] == 'media':
    incrementax = 2
else:
    incrementax = 3

alien_1['posicionx']=alien_1['posicionx'] + incrementax 
print("Nueva posicion x:" + str(alien_1['posicionx']))

# Eliminando una clave
print(alien_0)
del alien_0['puntos']
print(alien_0)

# Diccionario de lenguajes
lenguajes_favoritos={
    'jen' : 'python',
    'Sara' : 'c',
    'Ramon' : 'ruby',
    'Erika' : 'python'
}

print("El lenguaje favorito de Sara es " + lenguajes_favoritos['Sara'] + ".")

for nombre, lenguaje in lenguajes_favoritos.items():
    print("\nNombre:" + nombre)
    print("\nLenguaje:" + lenguaje)

for nombre, lenguaje in lenguajes_favoritos.items():
    print(lenguaje.title() + " es el lenguaje favorito de " + nombre.title() + ".")



# Recorriendo un diccionario
usuario_0={
    'nombre':'Juan',
    'primer_apellido':'Fernandez',
    'segundo_apellido':'Lopez'
}

for llave,valor in usuario_0.items():
    print("\nLLave: " + llave)
    print("\nValor: " + valor)


# Diccionario de lenguajes
lenguajes_favoritos={
    'jen' : 'python',
    'Sara' : 'c',
    'Ramon' : 'ruby',
    'Erika' : 'python'
}

amigos = ['Erika', 'sara']
for nombre in lenguajes_favoritos.keys():
    print(nombre.title())

    if nombre in amigos:
        print("Hola " + nombre.title() + " tu lenguaje favorito es " + lenguajes_favoritos[nombre].title())

# Recorriendo un Diccionario en orden
for nombre in sorted(lenguajes_favoritos.keys()):
    print(nombre.title() + " gracias por todo")

# Recorriendo los lenguajes
print("Los lenguajes mencionados son:")
for lenguaje in sorted(lenguajes_favoritos.values()):
    print(lenguaje.title())

# Omitiendo los lenguajes repetidos
print("Los lenguajes mencionados son:")
for lenguaje in set(lenguajes_favoritos.values()):
    print(lenguaje.title())

# Lista de Diccionarios
alien_0={'color':'green', 'points':5}
alien_1={'color':'yellow', 'points':10}
alien_2={'color':'red', 'points':15}

# Metemos en una lista todos los diccionarios
aliens=[alien_0,alien_1,alien_2]

# Recorremos la lista
for alien in aliens:
    print(alien)

# Creamos una lista vacia para guardar los aliens
aliens = []

# Creamos 30 aliens
for alien_number in range(30):
    new_alien={'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

# Mostramos los 5 primeros aliens
for alien in aliens[:5]:
    print(alien)
print("........")

# Mostramos todos los aliens creados
print("Total aliens:"+str(len(aliens)))

# Modificando aliens
for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10

# Mostramos los 5 primeros aliens
for alien in aliens[0:5]:
    print(alien)
    print(alien)
print("........")

# Un diccionario en un diccionario
usuarios= {
    'aenstein':{'nombre':'Arbert', 'apellidos':'einstein', 'lugar de nacimiento':'Princeton'},
    'mcurie':{'nombre':'Marie', 'apellidos':'Curie', 'lugar de nacimiento':'Paris'},
}

for usuario, informacion_usuario in usuarios.items():
    print("\nUsuario:" + usuario)
    nombre_completo = informacion_usuario['nombre'] + " " + informacion_usuario['apellidos']
    localidad = informacion_usuario['lugar de nacimiento']

    print("\nNombre completo:" + nombre_completo.title())
    print("\nLocalidad:" + localidad.title())
        







