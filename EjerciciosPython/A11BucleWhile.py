# Bucle while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# Dejar al usuario que elija cuando salir del bucle
texto = "\nIntroduce un texto:"
texto += "\nIntroduce 'salir' para abandonar el programa"
print(texto)
mensaje = ""
while mensaje != 'salir':
    mensaje = input(mensaje)
    print("Recibido:" + mensaje)

# Usando un flag
activo = True
while activo:
    mensaje = input(texto)
    if mensaje == 'salir':
        activo = False
    else:
        print(mensaje)
# Usando break para salir del bucle
text = "\nIntroduce la ciudad que has visitado:"
text += "\nIntroduce 'salir' para quitar el programa:"

while True:
    ciudad = input(text)
    if ciudad == 'salir':
        break
    else:
        print("He visitado " + ciudad.title() + " !")

# Usando continue
numero_actual = 0
while numero_actual < 10:
    numero_actual += 1
    if numero_actual % 2 == 0:
        continue
    print(numero_actual)

# Usar un bucle while con listas y diccionarios
# Lista con usuarios que necesitan ser verificados
usuarios_sin_confirmar = ['Alice', 'Brian', 'Candance']
# Lista vacia para usuarios confirmados
usuarios_confirmados = []

#Verificar a cada usuario hasta que no haya más usuarios sin confirmar.
# Mover cada usuario verificado a la lista de usuarios confirmados.
while usuarios_sin_confirmar:
    usuario_actual = usuarios_sin_confirmar.pop()

    print("Verificando usuario: " + usuario_actual.title())
    usuarios_confirmados.append(usuario_actual)

# Mostrar usuarios confirmados
print("\nLos siguientes usuarios han sido confirmados:")
for usuario_confirmado in usuarios_confirmados:
    print(usuario_confirmado.title())

# Eliminar todas las instancias de valores específicos de una lista
mascotas = ['perro', 'gato', 'perro', 'pescado', 'gato', 'conejo', 'gato']
print(mascotas)

while 'gato' in mascotas:
    mascotas.remove('gato')

print(mascotas)

# LLenar un diccionario con datos de entrada del usuario
respuestas = {}
# Poner un flag para indicar que la votacion esta activa.
votacion_activa = True
while votacion_activa:
    # Preguntas y respuestas.
    nombre = input("\nCual es tu nombre? ")
    respuesta = input("Que montaña te gustaria escalar hoy? ")
    # Almacenamos las respuestas en el diccionario:
    respuestas[nombre] = respuesta
    # Averiguar si alguien mas participa en la encuesta.
    repetir = input("Le gustaria que otra persona responda? (si/ no) ")
    if repetir == 'no':
        votacion_activa = False
# Polling is complete. Show the results.
print("\n--- Resultados de la Encuesta ---")
for nombre, respuesta in respuestas.items():
    print(nombre + " te gustaria escalar  " + respuesta + ".")






