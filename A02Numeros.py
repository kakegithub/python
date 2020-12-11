
# Numeros Enteros (integer)
# Puedes sumar (+), restar (-), multiplicar (*) y dividir (/) enteros en Python.
sumar = 2 + 3
restar = 3 - 2
multiplicar = 2 * 3
dividir = 3 / 2

print("Suma:",sumar)
print("Resta:",restar)
print("Multiplicacion:",multiplicar)
print("Division:",dividir)

# Representando exponentes
elevar = 3 ** 2
print("Potencia:",elevar)

'''Python también admite el orden de las operaciones, por lo que puede usar múltiples
operaciones en una expresión. También puede utilizar paréntesis para modificar el
orden de operaciones para que Python pueda evaluar su expresión en el orden
tu específicas.'''

exp1 = 2 + 3 * 3
exp2 = (2 + 3) * 4

print(exp1)
print(exp2)

# Numeros Decimales (float)
sumar = 0.1 + 0.1
restar = 0.4 - 0.2
multiplicar = 2 * 0.1
dividir = 0.3 / 0.2

print("Suma:",sumar)
print("Resta:",restar)
print("Multiplicacion:",multiplicar)
print("Division:",dividir)

# Evitar errores de tipo con la función str()
edad = 23
# Esto daria un error TypeError: can only concatenate str (not "int") to str
#mensaje = "Feliz " + edad + " cumpleaños"
#print(mensaje)

'''Cuando usas enteros dentro de cadenas debes especificar explícitamente 
que deseas que Python use el enterocomo una cadena de caracteres.'''
mensaje = "Feliz " + str(edad) + " cumpleaños"
print(mensaje)
