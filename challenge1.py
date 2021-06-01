from numpy import *
import numpy as np

values = str("values")
array = np.arange(0, 21)
no_mean = np.mean(array)
std = round(np.std(array), 2)
vari = round(np.var(array), 2)
print(array)
print(std)
print(vari)
