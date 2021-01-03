# CONDICIONALES
#Condicional If

print("Programa Evaluaciom Notas De Alumnos")

nota_alumno = input("Introduce la nota:") # Lo que introducimos con un input python lo considera texto por eso en la llamada
                                            # a la funcion ponemos evaluacion(int(nota_alumno))
def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Suspenso"
    return valoracion
print(evaluacion(int(nota_alumno))) # Transformamos nota_alumno en un entero

