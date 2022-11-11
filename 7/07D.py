import numpy as np


def format(value):
    return ('%.3f' % value).rstrip('0').rstrip('.')

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / float(N)

with open("input.txt", "r") as file:
    n, m = map(int, file.readline().split())
    arr = np.array(file.readline().split()).astype('double')

count = int(n - (m / 2))
with open("output.txt", "w") as result:
    # [format(arr[i:i + m].mean()) for i in range(count)]
    result.write(' '.join([format(i) for i in moving_average(arr, m)]))
