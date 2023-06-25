def factorial(n):
    print(f"factorial({n})")
    result = 1 if n <= 1 else n * factorial(n-1)
    print("returning", result)
    return result


factorial(4)
factorial(4)
factorial(3)
factorial(2)
factorial(1)


