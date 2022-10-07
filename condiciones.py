import sys

def evaluacion(nota):


	if nota<5:

		print("Insuficiente")

	elif nota < 7:
		print("Suficiente")

	elif nota < 9:
		print("Bien")

	else:
		print("Excelente")


print("Programa de evaluacion")

calificacion = int(input("Intruduce la calificacion: "))
asignatura = input("Introduce asignatura: ")

evaluacion(calificacion)

print("Fin del programa ")


lista=("fisica", "quimica","matematicas", "Estadistica")

listaNUM = (1,2,3,4,5,6,7,8,9,10)

if calificacion in listaNUM and asignatura.lower() in lista :
	print("OK " + str(calificacion))

else:
	print("NOK " + str(calificacion))


print(sys.version)
