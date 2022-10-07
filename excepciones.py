
print("Prueba de excepciones")

while True:
	try:
		a=(float(input("Introduce un numero: ")))
		b=(float(input("Introduce un numero: ")))
		break

	except ValueError:
		print("Valor incorrecto. Intentalo de nuevo")


try:
	c = a/b 
except ZeroDivisionError:
	print("No se puede dividir entre cero")
else:
	print("Resultado: ",c)
finally:
	print("Gracias por ejecutar este programa")

print("Adios!!")
