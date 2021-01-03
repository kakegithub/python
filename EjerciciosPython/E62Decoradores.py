# Decoradores con parametros
print("-----Ejemplo Decorador con parametros------------")

def funcionDecoradora(funcionParametro):
    # con *args le podemos pasar los argumentos que queramos
    # con **kwargs le podemos pasar parametros clave-valor
    def funcionInterior(*args, **kwargs): 
        # Acciones adicionales que decoran

        print("Vamos a realizar un calculo: ")
        funcionParametro(*args, **kwargs)

        # Acciones adicionales que decoran
        print("Hemos terminado el calculo: ")

    return funcionInterior

# Decoramos la funcion suma
@funcionDecoradora
def suma(num1, num2, num3):
    print(num1 + num2 + num3)

@funcionDecoradora
def resta(num1, num2):
    print(num1-num2)

@funcionDecoradora
def potencia(base, exponente):
    print(pow(base,exponente))


suma(7,5,8)
print("-----------------------")

resta(9,10)
print("-----------------------")

# Esto seria sin **kwargs
#potencia(5,2)
# Con kwargs seria
potencia(base=5, exponente=2)