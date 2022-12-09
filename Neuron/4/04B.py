import numpy as np
from matplotlib import pyplot as plt


import numpy as np


Oracle = None
class GDM:
    '''Represents a Gradient Descent with Momentum optimizer

    Fields:
        eta: learning rate
        alpha: exponential decay factor
    '''

    eta: float
    alpha: float

    def __init__(self, *, alpha: float = 0.9, eta: float = 0.1):
        '''Initalizes `eta` and `alpha` fields'''
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
        alpha = self.alpha
        beta = self.eta
        for _ in range(max_iter):
            grad = oracle.gradient(x)
            if np.linalg.norm(grad) < eps:
                return x
            v = alpha * v + beta * grad
            x = x - v
            # v = beta * v + (1-beta) * grad
            # x = x - alpha * v
        return x



class Oracle:
    '''Provides an interface for evaluating a function and its derivative at arbitrary point'''

    def value(self, x: np.ndarray) -> float:
        '''Evaluates the underlying function at point `x`

        Args:
            x: a point to evaluate funciton at

        Returns:
            Function value
        '''
        return x**2

    def gradient(self, x: np.ndarray) -> np.ndarray:
        '''Evaluates the underlying function derivative at point `x`

        Args:
            x: a point to evaluate derivative at

        Returns:
            Function derivative
        '''
        return 2 * x

alph = 0.95
eta = 0.9
orac = Oracle()
gdm = GDM(alpha = alph, eta = eta)
xs = gdm.optimize(orac, 1)
print(xs)
xp = np.linspace(-1.2, 1.2, 100)
# plt.plot(xp, orac.value(xp))
# plt.plot(xs, orac.value(xs), 'o-', c='red')
# for i, (x, y) in enumerate(zip(xs, orac.value(xs)), 1):
#     plt.text(x, y+0.2, i,
#              bbox=dict(facecolor='yellow', alpha=0.5), fontsize=14)
# pass
