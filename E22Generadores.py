# Generadores concepto
# Estructuras que extraen valores de una funcion y se almacenan en objetos iterables (que se pueden recorrer)
# Estos valores se almacenan de uno a uno
# Son mas eficientes que las funciones tradicionales
# Muy utiles con listas de valores infinitos
# Bajo determinados escenarios es muy util que devuelva los valores de uno en uno


# Utilizando una funcion
def generaPares(limite):
    
    num = 1
    miLista=[] # lista para almacenar los numeros
    
    while num < limite:
        miLista.append(num*2) # Multiplicamos num * 2
        num=num+1 # Incrementamos el valor de num
        
    return miLista

print(generaPares(10))

# Ejemplo generador # Un generador puede llevar opcionalmente un return
def generaPar(limite):
    
    num = 1
    
    while num < limite:
        yield num*2
        num=num+1 # Incrementamos el valor de num
        
devuelvePar=generaPar(10) # Almacenamos el valor

#for i in devuelvePar: # Devuelve la lista entera
#    print(i)

print(next(devuelvePar)) # Devuelve objeto 2

print("Aqui podria ir mas codigo")

print(next(devuelvePar)) # Devuelve objeto 4
    
print("Aqui podria ir mas codigo")




