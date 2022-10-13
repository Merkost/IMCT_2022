def counter_decorator(func):
    def wrapper(a, b):
        wrapper.calls += 1
        print(f"Function calls count: {wrapper.calls}")
        return func(a,b)
    wrapper.calls = 0
    return wrapper

def projection_decorator(func):
    def wrapper(x,y,z):
        func(3*x - 7*y + 15*z + 18)
    return wrapper


def sum(a: int, b: int):
    print(a + b)


fn = counter_decorator(sum)
fn(1, 2)
fn(4, 5)
fn(-4, 5)





@projection_decorator
def calc(x: int):
    print(x * x)

calc(1, 2, 3)