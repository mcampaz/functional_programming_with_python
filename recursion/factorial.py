from functools import reduce


def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n - 1)
    print(f"factorial({n}) returns {return_value}")
    return return_value


factorial(10)


def loop_factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value


print(f"Factorial using loops: {loop_factorial(4)}")


def reduce_factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1) or [1])


print(f"Factorial using reduce tool: {reduce_factorial(0)}")
