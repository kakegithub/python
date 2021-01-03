# Crea un programa que pida tres números por teclado. 
# El programa imprime en consola la media aritmética de los números introducidos.

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
num3 = int(input("Introduce un numero: "))

def mediaAritmetica(a,b,c):
    media = (a+b+c)/3
    return media

almacena_media = mediaAritmetica(num1,num2,num3)
print(almacena_media)


