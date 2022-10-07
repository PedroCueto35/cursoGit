class Persona():

	def __init__(self, nombre, edad, Lugar_residencia):

		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=Lugar_residencia

	def descripcion(self):

		print("Nombre: ",self.nombre, ", Edad: ",self.edad, ", Residencia: ",self.lugar_residencia)

class Empleado(Persona):		

	def __init__(self, salario, antiguedad, nombre, edad, residencia):

		super().__init__(nombre, edad, residencia)

		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):

		super().descripcion()
		print("Salario: ",self.salario, "Antiguedad: ",self.antiguedad)


Manuel=Empleado(1500, 15, "Manuel", 55, "Mexico")
Manuel.descripcion()

print(isinstance(Manuel, Persona))

Pedro = Persona("Pedro", 39, 'Mexico')
Pedro.descripcion()


print(isinstance(Pedro, Empleado))


