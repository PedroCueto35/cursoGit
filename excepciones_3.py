import math

def raizCuadrada(num):

    if num < 0:
        raise ValueError ("El numero no puede ser negativo")

    else:
        return math.sqrt(num)


numero = float(input("Intoduce un numero: "))

try: 
    print(raizCuadrada(numero))
except ValueError as errNeg:

    print(errNeg)

print("Fin del programa")