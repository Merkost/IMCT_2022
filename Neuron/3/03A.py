import math
import matplotlib.pyplot


def func(x):
    return x ** 3 - 2 * x ** 2 + 50 * math.sin(5 * x) + 3


def draw(plt: matplotlib.pyplot, x: list) -> None:
    y = [func(i) for i in x]
    plt.grid()
    plt.xlabel('$x$')
    plt.ylabel('$x^3-2x^2+50sin(5x)+3$')
    plt.plot(x, y, color='green')


draw(matplotlib.pyplot, [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
