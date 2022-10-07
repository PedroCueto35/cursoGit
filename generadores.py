"""
def generaPares(Limite):

    num = 1

    miLista = []

    while num < Limite:
        miLista.append(num*2)

        num += 1

    return miLista
"""

#Utilizando un generador
def generaPares(Limite):

    num = 1

    while num < Limite:
        yield num * 2

        num += 1

devueldePares = generaPares(10)

#for i in devueldePares:

#    print(i)

print(next(devueldePares))

print("otro codigo")

print(next(devueldePares))

print("otro codigo")

print(next(devueldePares))