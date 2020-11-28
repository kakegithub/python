# Metodos mas utilizados de la clase String
#upper()------------>Convierte en mayusculas todas las letras de un String
#lower()------------>Convierte en minusculas todas las letras de un String
#capitalize()------->Pone la primera letra en mayusculas
#count()------------>Cuenta cuantas veces aparece una letra o una cadena de caracteres en un texto
#find()------------->Representa la posicion de un caracter o grupo de caracteres en un texto
#isdigit()---------->Devuelve un booleano True/False si el valor introducido es numerico o no lo es
#isalum()----------->Comprueba si son valores alfanumericos
#isalpha()---------->Comprueba si hay solo letras 
#split()------------>Separa por palabras utilizando espacios
#strip()------------>Borra los espacios sobrantes al principio y al final
#replace()---------->Cambia una palabra o una letra por otra
#rfind()------------>Representa un indice de un caracter pero contando desde atras

nombreUsuario=input("Introduce tu nombre de usuario:")
print("El nombre es:",nombreUsuario.upper())
print("El nombre es:",nombreUsuario.lower())
print("El nombre es:",nombreUsuario.capitalize())

edad=input("Introduce tu edad:")
#print(edad.isdigit())
while(edad.isdigit()==False):
    print("Por favor introduce un valor numerico")
    edad=input("Introduce tu edad:")

if(int(edad)<18):
    print("No puedes pasar")
else:
    print("Puedes pasar")







