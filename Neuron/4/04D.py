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

class AdaGrad:
    '''Represents an AdaGrad optimizer

    Fields:
        eta: learning rate
        epsilon: smoothing term
    '''

    eta: float
    epsilon: float

    def __init__(self, *, eta: float = 0.1, epsilon: float = 1e-8):
        '''Initalizes `eta` and `epsilon` fields'''
        self.eta = eta
        self.epsilon = epsilon

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
        # d-dimensional vector representing diag(Gt) to store a running total of the squares of the gradients.
        gti = np.zeros(x0.shape[0])
        for t in range(max_iter):
            grad = oracle.gradient(x)
            gti += grad ** 2
            adjusted_grad = grad / (self.epsilon + np.sqrt(gti))
            if np.linalg.norm(grad) < eps:
                return x
            x = x - self.eta * adjusted_grad
        return x

















def AdaGrad(data, theta, lr = 1e-2, epsilon = 1e-8, num_iterations = 100):
    loss = []
    #initialize gradients_sum for storing sum of gradients
    gradients_sum = np.zeros(theta.shape[0])
    for t in range(num_iterations):
        #compute gradients with respect to theta
        gradients = compute_gradients(data, theta)
        #compute square of sum of gradients
        gradients_sum += gradients ** 2
        #update gradients
        gradient_update = gradients / (np.sqrt(gradients_sum + epsilon))
        #update model parameter according to equation (12)
        theta = theta - (lr * gradient_update)
        loss.append(loss_function(data,theta))
    return loss