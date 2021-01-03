#Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” 
# encargada de devolver el número más alto de los dos introducidos.

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

def DevuelveMax(num1, num2):
    
    if num1 > num2:
        maximo = num1
    elif num1 < num2:
        maximo = num2
    else:
        maximo = num1
    return maximo

almacena_maximo = DevuelveMax(num1, num2)
print("Maximo: " + str(almacena_maximo))
