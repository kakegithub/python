#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. 
# Esos tres datos deberán ser almacenados en una lista y mostrar en consola 
# el mensaje: “Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).

Nombre = input("Introduce el Nombre: ")
Direccion = input("Introduce la Direccion: ")
Telefono = int(input("Introduce el Telefono: "))

datosPersonales=[]

datosPersonales.append(Nombre)
datosPersonales.append(Direccion)
datosPersonales.append(Telefono)

print("Los Datos personales son: " + datosPersonales[0] + " " + datosPersonales[1] + " " + str(datosPersonales[2]))