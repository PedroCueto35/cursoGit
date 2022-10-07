
from datetime import datetime
import sys

fecha = datetime.now()

print(fecha)

cumple = "02/03/1986"

fec_paso = datetime.strptime(cumple, '%d/%m/%Y')

print(fec_paso.day)

fec_cumple = datetime.strftime(fec_paso, '%Y%m%d')

print(fec_cumple)

print(sys.version)



