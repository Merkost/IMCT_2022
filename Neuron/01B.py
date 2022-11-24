import numpy as np
import scipy as sp

# n = int(input())
# y = input().split()
x = np.array([1, 2, 3, 4, 5])
y = np.array([30, 50, 80, 160, 300])
f = sp.interpolate.interpn(x, y, fill_value = "extrapolate")
for i in range(0, 6):
    print(f(i))

"""
    
5
700.949074 715.616206 726.958614 730.983909 730.427020

"""