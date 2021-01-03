''' Funcion Filter verifica que los elementos de una secuencia cumplen una condicion
    devolviendo un iterador con los elementos que cumplen dicha condicion'''

'''def numeroPar(num):
    if num % 2 == 0:
        return True

numeros=[17,24,739,8,51,92]

print(list(filter(numeroPar, numeros)))

# Haciendolo con una funcion lambda
print(list(filter(lambda numeroPares: numeroPares % 2 == 0, numeros)))'''


# Otro Ejemplo
class Empleado:
    def __init__(self, nombre, cargo, salario):
        super().__init__()
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} € ".format(self.nombre,self.cargo,self.salario)

    
listaEmpleados=[
    Empleado("Juan", "Director", 75000),
    Empleado("Ana", "Presidenta", 85000),
    Empleado("Antonio", "Administrativo", 25000),
    Empleado("Sara", "Secretaria", 27000),
    Empleado("Mario", "Botones", 21000),
]

salariosAltos=filter(lambda empleado:empleado.salario > 50000, listaEmpleados)

for empleadoSalario in salariosAltos:
    print(empleadoSalario)





