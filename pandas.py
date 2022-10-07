# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
"""
Editor de Spyder

Este es un archivo temporal.
"""
print("hola")

a = 34

print(a)

data = np.array([['','Col1','Col2'],
                ['Row1',1,2],
                ['Row2',3,4]])

print(data)

print(pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:]))

