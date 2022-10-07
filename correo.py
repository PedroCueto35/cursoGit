print("---------- Validacion de correo --------------")

correo = input("Introduce tu correo: ")

val = False

for i in correo:

	if i == "@":

		val = True

if val:
	print("Correo OK")
else:
	print("Correo erroneo")


for i in range(3,20,7):
	print(f"Valor de la variable: {i}")
	

