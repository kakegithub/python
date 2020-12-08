# Funciones decoradores añaden funcionalidad a otras funciones

# Estructura decorador (A,B,C) donde A recibe como parametro B para devolver C

# Un decorador devuelve una funcion

''' def funcionA(funcionB):
        def funcionC():
            # Codigo de la funcionC
        return funcionC '''

print("-----Ejemplo Decorador------------")

def funcionDecoradora(funcionParametro):
    def funcionInterior():
        # Acciones adicionales que decoran

        print("Vamos a realizar un calculo: ")
        funcionParametro()

        # Acciones adicionales que decoran
        print("Hemos terminado el calculo: ")

    return funcionInterior

# Decoramos la funcion suma
@funcionDecoradora
def suma():
    print(15 + 20)

@funcionDecoradora
def resta():
    print(30-10)

suma()
print("-----------------------")
resta()




