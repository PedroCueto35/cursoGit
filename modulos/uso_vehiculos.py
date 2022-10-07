from modulo_vehiculos import *

miCoche = Vehiculos("Mazda","MX5")
miCoche.acelerar()

miCoche.estado()

print("-------------------------------------------------------")

miFurgoneta = Furgoneta("Chevrolet",'XAZ11')

miFurgoneta.arrancar()
miFurgoneta.acelerar()
miFurgoneta.estado()
print(miFurgoneta.carga(False))