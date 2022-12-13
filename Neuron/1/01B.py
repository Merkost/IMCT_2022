import numpy as np
import scipy as sp

def fr(x):
    return 5 + np.sin(x)*2.546479*np.pi + 7*x

# n = int(input())
# y = input().split()
x = np.array([1, 2, 3, 4, 5])
# y = np.array([30, 50, 80, 160, 300])
y = np.array([700.949074, 715.616206, 726.958614, 730.983909, 730.427020])
f = sp.interpolate.interp1d(x, y, fill_value = "extrapolate")
for i in range(0, 7):
    print(f(i))

# import numpy as np
#
# def f(x):
#   return 5 + np.sin(x)*2.546479*np.pi + 7*x
#
# def rev_f(y):
#   return (y - 5) / (7)
# N = int(input())
# extra_mas = list(map(float, input().split()))
#
# rarety = int(round(rev_f(extra_mas[-1])))-3
#
# for i in range(rarety, rarety + 6):
#   fnc = f(i)
#   if abs(fnc - extra_mas[-1]) < 0.0001:
#     print(f(i+1))
#     break

"""
    
5
700.949074 715.616206 726.958614 730.983909 730.427020

"""