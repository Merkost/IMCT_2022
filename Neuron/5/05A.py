"""

Линейная регрессия. Основы
"""

import numpy as np

def linear_func(theta, x):                  # function value
    return theta @ x
def linear_func_all(theta, X):              # 1-d np.array of function values of all rows of the matrix X
    return X @ theta
def mean_squared_error(theta, X, y):        # MSE value of current regression
    return np.mean((y - linear_func_all(theta, X))**2)
def grad_mean_squared_error(theta, X, y):   # 1-d array of gradient by theta
    return np.mean((linear_func_all(theta, X) - y) * 2 * X.T, axis = 1)

X = np.array([[1,2],[3,4],[4,5]])
theta = np.array([5, 6])
y = np.array([1, 2, 1])
func = linear_func_all(theta, X) # --> array([17, 39, 50])
print(func)
mean = mean_squared_error(theta, X, y) # --> 1342.0
print(mean)
error = grad_mean_squared_error(theta, X, y) # --> array([215.33333333, 283.33333333])
print(error)