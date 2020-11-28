# Operador IN

print("Asignaturas Optativas año 2020")
print("informatica basica - pruebas de sofware - usabilidad y accesibilidad")

asignatura = input("Escoja la asignatura escogida: ")
opcion = asignatura.lower()
print ("Asignatura escogida: " + opcion)

if opcion in("informatica basica","pruebas de sofware","usabilidad y accesibilidad"):
    print("Asignatura elegida:" + opcion)
else:
    print("La asignatura no esta contemplada")

