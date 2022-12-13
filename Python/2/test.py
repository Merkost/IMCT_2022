def counter_decorator(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function calls count: {wrapper.calls}")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def projection_decorator(func):
    def wrapper(x, y, z):
        func(3 * x - 7 * y + 15 * z + 18)
    return wrapper


@projection_decorator
def calc(x: int):
    print(x * x)


calc(1, 2, 3)
