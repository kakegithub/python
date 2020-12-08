# Funciones lambda

'''def areaTriangulo(base, altura):

    return (base*altura)/2

#print(areaTriangulo(5,7))  

triangulo1=areaTriangulo(5,7)

triangulo2=areaTriangulo(9,6)

print(triangulo1)

print(triangulo2)'''

areaTriangulo=lambda base,altura:(base * altura)/2

triangulo1=areaTriangulo(5,7)

triangulo2=areaTriangulo(9,6)

print(triangulo1)

print(triangulo2)

alCubo=lambda numero:pow(numero,3)
print(alCubo(13))

destacarValor=lambda comision:"¡{}! €".format(comision)

comision_Ana=15585

print(destacarValor(comision_Ana))

