3 # Listas en python

# Creacion de una Lista
bicicletas = ['treck', 'cannondale', 'redline', 'specialized']

# Mostrar lista
print(bicicletas)
print('------------------------------')
# Acceder a los elemnetos de una lista
print(bicicletas[0])
print(bicicletas[1])
print(bicicletas[2])
print(bicicletas[3])
print('--------------------------------')
#Acceder a los elemnetos de una lista desde el final
print(bicicletas[-1])
print(bicicletas[-2])
print(bicicletas[-3])
print(bicicletas[-4])
print('---------------------------------')
# Recorerr todos los elemntos de una lista
for elemento in bicicletas:
    print(elemento)
print('------------BICICLETAS-----------------------')
# Formatear un elemnto
print(bicicletas[0].title())
print('------------BICICLETAS------------------------')

# Mensaje personalizado
mensaje = "Mi primera bicicleta era una " + bicicletas[0].title() + "."
print(mensaje)
print("-------------MOTOS------------------------")

# Modificando elementos de una lista
motos = ["honda", "yamaha", "suzuki"]
print(motos)

# Modificamos un valor
motos[0] = "ducati"
print(motos)
print("--------------MOTOS---------------------------")

# Añadiendo elementos a la lista
motos.append("derbi")
print(motos)
print("---------------MOTOS---------- --")

# Insertar elementos en una posicion de la lista
motos.insert(0, "bultaco")
print(motos)
print("----------------MOTOS--------------------")

# Remover elementos de la lista
del motos[0]
print(motos)

del motos[3]
print(motos)
print("---------------MOTOS------------------------")
# Eliminar un elemento mediante el método pop()
#El método pop() elimina el último elemento de una lista, pero le permite trabajar con ese elemento después de quitarlo.

popped_motos = motos.pop()
print(popped_motos)
print("-----------")
print(motos)
print("------------")
print("Mi ultima moto fue una " + popped_motos.title())

# Se puede usar pop() para eliminar un elemento de una lista en cualquier posición
# pasandole la posicion entre parentesis
print("-----------Motos---------------")
print(motos)
primera_moto = motos.pop(0)
print(primera_moto)
print("Mi primera moto fue una " + primera_moto.title())

# Removiendo un item por valor
print('----------MOTOS--------------')
print("Vamos a añadir algunos elementos a la lista")
motos.append("Derbi")
motos.append("Bultaco")
motos.append("Honda")
print(motos)
print("Vamos a eliminar bultaco")
motos.remove("Bultaco")
print(motos)
print("Removiendo elemento de lista asignado a variable")
moto_barata="Derbi"
motos.remove(moto_barata)
print(motos)
print("La moto " + moto_barata.title() + " tiene un precio ajustado")
# Derbi ha sido borrado de la lista pero aun permanece en la variable moto_barata
# El metodo remove() solo borra la primera ocurrencia de la lista. 
# Necesitamos un bucle para saber si todas las ocurrencias de la lista han sido removidos





