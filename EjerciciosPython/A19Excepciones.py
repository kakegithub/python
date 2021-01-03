# Tratamiento de excepciones
"""try:
    print(5/0)
except ZeroDivisionError as identifier:
    print("No se puede dividir entre cero")"""

# Otro ejemplo
print("Introduce dos numeros, y hare una division.")
print("Introduce 'q' para salir.")
while True:
    numero1 = input("\nnumero1: ")
    if numero1 == 'q':
        break
    numero2 = input("numero2: ")
    try:
        respuesta = int(numero1) / int(numero2)
    except ZeroDivisionError:
        print("No puedes dividir por 0!")
    else:
        print(respuesta)

# Otro ejemplo
archivo = 'alicia.txt'
try:
    with open(archivo) as file_object:
        contenido = file_object.read()
except FileNotFoundError:
    print("No se pudo encontrar el archivo solicitado")

# analizando texto
titulo = "Alicia en el pais de las maravillas"
print(titulo.split())


