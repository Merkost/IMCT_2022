import numpy as np
from math import *


def nearest(points: np.ndarray, a: np.ndarray) -> np.ndarray:
    '''Returns the point from `points` nearest to `a` in terms of euclidean distance

    Args:
        points: A 2-dimensional np.ndarray
        a: A 1-dimensional np.ndarray, `a`.shape[0] == `points`.shape[1]

    '''
    for point in points:
        print(point - np.array([9,9]))
    # print([[f"{a}, {b}" for a, b in zip(np.array(point), a.repeat(points.size))] for point in points])
    distances = np.array(np.sqrt(np.sum(pow(a - point, 2))) for point in points)
    # distances = np.array(np.sqrt(sum(pow(a - b, 2) for a, b in [zip(point, a) for point in points])))
    # distance = np.sqrt(sum(pow(a - b, 2) for a, b in zip(point_1, point_2)))

    return distances

print(*nearest(np.array([[0, 0], [3, 3]]), np.array([1, 1])))
