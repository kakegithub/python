
# Metodo super()----> llama al metodo de la clase padre
# isinstance()------> Nos informa si un objeto es instancia de una clase determinada (True/False)

class Persona():
    
    def __init__(self, nombre, edad, lugar_residencia):
        
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Lugar de residencia: ", self.lugar_residencia)


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, lugar_residencia_empleado):
        
        super().__init__(nombre_empleado, edad_empleado, lugar_residencia_empleado) # LLama al constructor de la clase padre

        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, " antiguedad: ", self.antiguedad)

#Antonio=Persona("Antonio", 55, "España")
#Antonio.descripcion()

Manuel=Empleado(1500, 15, "Manuel", 55, "Colombia")
Manuel.descripcion()

# principio de sustitucion (Es un/a de)
print(isinstance(Manuel, Empleado)) # Manuel es un objeto de la clase Empleado
print(isinstance(Manuel, Persona)) # Manuel es un objeto de la clase Persona