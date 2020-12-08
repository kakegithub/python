# Documentacion

class Areas:

    """ Esta clase calcula las areas de diferentes figuras geometricas """

    def areaCuadrado(lado):
        ''' Calcula el area de un cuadrado elevando el lado pasado por parametro '''
        return "El area del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):
        '''Calcula el area de un triangulo utilizando los parametros base y altura '''
        return "El area del triangulo es " +str((base * altura)/2)


    #print(areaCuadrado(3))
    #print(areaCuadrado.__doc__) # Imprime la documentacion asociada a la funcion areaCuadrado()
    #print("---------------------------------")
    #help(areaCuadrado) # Imprime la documentacion asociada a la funcion areaCuadrado()
    #print(areaTriangulo(2,7))
    #help(areaTriangulo)#

help(Areas.areaTriangulo)
print("------------------------------")

help(Areas)
