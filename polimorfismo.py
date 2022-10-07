from datetime import datetime as fh

class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

class Bici():

    def camina(self):
        print("Voy solo")

def desplaza(vehiculo):
    vehiculo.desplazamiento()

print("Prueba de impresion de la hora", fh.today())
print("Prueba de impresion de la hora ...", fh.now().strftime("%H:%M:%S"))

micoche = Bici()
micoche.camina()
#desplaza(micoche)


v1=Moto()

v2=Coche()

v3=Camion()

desplaza(v2)
