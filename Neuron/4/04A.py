import numpy as np
import matplotlib.pyplot as plt

class GradientOptimizer:
    def __init__(self, oracle, x0):
        self.oracle = oracle
        self.x0 = x0

    def optimize(self, iterations, eps, alpha):
        x = self.x0
        for _ in range(iterations):
            grad = self.oracle.get_grad(x)
            if np.linalg.norm(grad) < eps:
                return x
            x = x - alpha * grad
        return x

class Oracle:
    def get_func(self, x): return x**2

    def get_grad(self, x): return 2*x

def f(x):
    return x ** 2


optimizer = GradientOptimizer(Oracle(), 1)
xs = optimizer.optimize(1000, 10e-1, 0.1)
xp = np.linspace(-1.2, 1.2, 100)
plt.grid()
plt.xlabel('xs')
plt.plot(xp, f(xp))
plt.plot(xs, f(xs), 'o-', c='red')
print(xs)
print("i love u")