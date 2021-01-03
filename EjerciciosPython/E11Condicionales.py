# Concatenacion operaciones de comparacion

# Primer ejemplo
edad = 7
if 0 < edad < 100:
    print("Edad correcta")
else:
    print("Edad incorrecta")

# Segundo ejemplo
salario_presidente = int(input("Introduce el salario del presidente: "))
print("Salario Presidente: " + str(salario_presidente))

salario_director = int(input("Introduce el salario del director: "))
print("Salario Director: " + str(salario_director))

salario_jefe_area = int(input("Introduce el salario del Jefe de Area: "))
print("Salario Jefe Area: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduce el salario del administrativo: "))
print("Salario Administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona bien")
else:
    print("Algo falla en esta empresa")



