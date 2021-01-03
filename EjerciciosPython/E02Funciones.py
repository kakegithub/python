#Funciones en Python
#def nombreFuncion():

def mensaje(): # Declaracion de la funcion
    print("Estamos aprendiendo python")
    print("Estamos aprendiendo instrucciones basicas")
    print("Poco a poco iremos avanzando")

mensaje() # LLamada a la funcion

# Paso de parametros a la funcion # Python pasa siempre los valores por referencia

def suma(num1, num2):
    print(num1 + num2)


suma(5,7)
suma(2.5,3.7)

# Usando return
def suma2(num1,num2):
    resultado = num1 + num2
    return resultado # Valor a devolver

almacena_resultado = suma2(5,5) # Valor lo almacenamos en una variable
print(almacena_resultado) # Mostramos resultado por pantalla





