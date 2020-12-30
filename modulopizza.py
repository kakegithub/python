
def hacer_pizza(tamano, *ingredientes):
    print("Ingredientes de la pizza " + str(tamano))
    for ingrediente in ingredientes:
        print("-" + ingrediente)