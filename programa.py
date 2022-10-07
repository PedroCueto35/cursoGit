def area(b,a):
	A = b*a/2
	return A

def imprime(a):
	print("El area del triangulo es: ", a)


area = area(7,5)

imprime(area)

lista=[4,True,"Hola",87.44,False,"Casa",3.1415,["pedro",4]]

print("impresion1 ",lista)

print("impresion2 ",lista[5:])

print("impresion3 ",lista[:2])

print("impresion4 ",lista[1:4])

print("impresion5 ",lista[-2])

lista.insert(4,"PedroCueto")

print(lista)

lista.append(999)

print(lista)

for i in lista:
	print(i)


