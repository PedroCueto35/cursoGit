class Movil():

	def __init__(self):

		self.__marca = "Motorola"
		self.__modelo = "One"
		self.__operador = "Orange"
		self.__encendido = False
		self.__precio = 350

	def encender(self, encendemos):
		self.__encendido=encendemos

		if self.__encendido:
			chequeo=self.__chequeo_inicial()

		if self.__encendido and chequeo:
			return "El movil esta encendido"

		elif self.__encendido and not chequeo:
			return "Algo fue mal en el chequeo"

		else:
			return "El movil esta apagado"

	def estado(self):
		print("La marca del movil es ", self.__marca, "el modelo es ", self.__modelo,
		 "el operador es ", self.__operador, " y el precio es: ", self.__precio)


	def __chequeo_inicial(self):

		print("Realizando revision inicial")

		self.bateria="OK"
		self.senal="OK"

		if self.bateria=="OK" and self.senal=="OK":
			return True

		else:
			return False


miMovil=Movil()

print(miMovil.encender(True))

miMovil.estado()


print("---------------- Otro objeto ---------------------")

movil2=Movil()

print(movil2.encender(False))

movil2.estado()

print('---------- MAS OBJETOS ----------------')
movil3 = Movil()
print(movil3.encender(True))
movil3.estado()