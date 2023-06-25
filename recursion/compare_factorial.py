# compare_factorial.py

def recursive(n):
    return 1 if n <= 1 else n * recursive(n - 1)

def loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

from functools import reduce

def functional(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
