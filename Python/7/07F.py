import numpy as np

def format(value):
    return ('%.3f' % value).rstrip('0').rstrip('.')

with open("input.txt", "r") as file:
    n, m = map(int, file.readline().split())
arr = np.loadtxt("input.txt", skiprows=1)
coef = np.corrcoef(arr)



with open("output.txt", "w") as result:
    for row in coef:
        result.write(" ".join([format(i) for i in row]))
        result.write("\n")

