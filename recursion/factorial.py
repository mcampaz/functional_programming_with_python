from functools import reduce
from timeit import timeit
from math import factorial as fact


def factorial(n):
    # print(f"factorial() called with n = {n}")
    # return_value = 1 if n <= 1 else n * factorial(n - 1)
    # print(f"factorial({n}) returns {return_value}")
    # return return_value
    return 1 if n <= 1 else n * factorial(n - 1)

# factorial(10)


def loop_factorial(n):
    # print(f"factorial() called with n = {n}")
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value


def reduce_factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1) or [1])


# print(f"Factorial using reduce tool: {reduce_factorial(0)}")

print(f'Result, recursive math call: {timeit("factorial(4)", "from math import factorial", number=100000000)}')

print(f'Result, recursive call: {timeit("factorial(4)", "from __main__ import factorial", number=100000000)}')

print(f'Result, loop_factorial call: {timeit("loop_factorial(4)", "from __main__ import loop_factorial", number=100000000)}')

print(f'Result, reduce_factorial call: {timeit("reduce_factorial(4)", "from __main__ import reduce_factorial", number=100000000)}')



