import numpy as np


def format(value):
    return ('%.3f' % value).rstrip('0').rstrip('.')


with open("input.txt", "r") as file:
    n, m = map(int, file.readline().split())
    arr = np.array(file.readline().split()).astype('double')

count = int(n - (m / 2))
with open("output.txt", "w") as result:
    result.write(' '.join([format(arr[i:i + m].mean()) for i in range(count)]))
