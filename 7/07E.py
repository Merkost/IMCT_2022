import numpy as np


def format(value):
    return ('%.3f' % value).rstrip('0').rstrip('.')


def weighted_moving_average(x, weights, w_sum):
    return np.convolve(x, weights, 'valid') / w_sum


with open("input.txt", "r") as file:
    n, m = map(int, file.readline().split())
    weights = np.array(file.readline().split()).astype('int')
    arr = np.array(file.readline().split()).astype('double')

with open("output.txt", "w") as result:
    # result.write(' '.join([format(np.average(arr[j:j + m], weights=weights)) for j in range(int(n - m / 2))]))
    result.write(' '.join([format(i) for i in weighted_moving_average(arr, weights[::-1], float(weights.sum()))]))
