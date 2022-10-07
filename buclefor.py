
estaciones = ("primavera", "verano", "otoño", "invierno")

for i in (3,4):
	print(i)

	for j in estaciones:
		print(j, end="\n")

	print("-"*100)

nombre = "Pedro López Cueto"

for i in nombre:
	print(i, end=" ")

if "P" in nombre.upper():
	print("\nOK")

else:
	print("\nKO")
