
estaciones = ("primavera", "verano", "otoño", "invierno")

for i in (3,4):
	print(i)

	for j in estaciones:
		print(j, end="\n")

	print("-"*100)

nombre = "pedro Lopez Cueto"

for i in nombre:
	print("jaja ", end="")

if "P" in nombre.upper():
	print("OK")

else:
	print("KO")