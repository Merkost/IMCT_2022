import numpy as np
from scipy.stats import moment

def format(value):
    return ('%.3f' % value).rstrip('0').rstrip('.')

with open("input.txt", "r") as file:
    n, k = map(int, file.readline().split())
arr = np.loadtxt("input.txt", skiprows=1)
# moment = 1/n*(np.power((arr - arr.mean()), k))
moment = moment(arr, k)


with open("output.txt", "w") as result:
    result.write(format(moment[k]))

