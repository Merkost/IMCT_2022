import numpy as np


class Oracle:
    '''Provides an interface for evaluating a function and its derivative at arbitrary point'''

    def value(self, x: np.ndarray) -> float:
        '''Evaluates the underlying function at point `x`

        Args:
            x: a point to evaluate funciton at

        Returns:
            Function value
        '''
        raise NotImplementedError()

    def gradient(self, x: np.ndarray) -> np.ndarray:
        '''Evaluates the underlying function derivative at point `x`

        Args:
            x: a point to evaluate derivative at

        Returns:
            Function derivative
        '''
        raise NotImplementedError()

import numpy as np
import math

class NesterovAG:
    '''Represents a Nesterov Accelerated Gradient optimizer

    Fields:
        eta: learning rate
        alpha: exponential decay factor
    '''

    eta: float
    alpha: float

    def __init__(self, *, alpha: float = 0.9, eta: float = 0.1):
        '''Initalizes `eta` and `aplha` fields'''
        self.eta = eta
        self.alpha = alpha

    def optimize(self, oracle, x0: np.ndarray, *,
                 max_iter: int = 100, eps: float = 1e-5) -> np.ndarray:
        '''Optimizes a function specified as `oracle` starting from point `x0`.
        The optimizations stops when `max_iter` iterations were completed or
        the L2-norm of the gradient at current point is less than `eps`

        Args:
            oracle: function to optimize
            x0: point to start from
            max_iter: maximal number of iterations
            eps: threshold for L2-norm of gradient

        Returns:
            A point at which the optimization stopped
        '''
        x = x0
        v = 0
        eta = self.eta
        alpha = self.alpha

        for _ in range(max_iter):
            gradient = oracle.gradient(x)
            if np.linalg.norm(gradient) < eps:
                return x
            v = alpha * v + eta * oracle.gradient(x - alpha * v)
            x = x - v
        return x