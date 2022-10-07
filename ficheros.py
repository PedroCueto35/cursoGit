
fentrada = open("TKLGDUSA.TXT","r")

for linea in fentrada.readlines():
	
	linea=linea.replace("\n","")
	linea=linea.replace(" ","")

	print(type(linea))

	reg=linea.split(",")
	print(type(reg))

	print(reg)
