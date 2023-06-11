# The perfect data structure for storing this data could be
# a Python list comprehension nested within a dictionary comprehension:
from pprint import pprint
import random
import timeit
#
# cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
# temps = {city: [0 for _ in range(7)] for city in cities}
# pprint(f"Cities in set: {temps}")

# {
#     'Austin': [0, 0, 0, 0, 0, 0, 0],
#     'Tacoma': [0, 0, 0, 0, 0, 0, 0],
#     'Topeka': [0, 0, 0, 0, 0, 0, 0],
#     'Sacramento': [0, 0, 0, 0, 0, 0, 0],
#     'Charlotte': [0, 0, 0, 0, 0, 0, 0]
# }

#
# Nested lists are a common way to create matrices,
# which are often used for mathematical purposes.
# Take a look at the code block below:
#

matrix = [[i for i in range(5)] for _ in range(6)]
pprint(f"matrix in list comprehension: {matrix}")
# [
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4]
# ]
#
#
# Take this example, which uses a nested list comprehension to flatten a matrix:
#
#
matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
]
flat = [num for row in matrix for num in row]
print(f"Matrix flattened: {flat}")
# [0, 0, 0, 1, 1, 1, 2, 2, 2]
#
#
# On the other hand, if you were to use for loops to flatten the same matrix,
# then your code will be much more straightforward:
#
#
# matrix = [
#     [0, 0, 0],
#     [1, 1, 1],
#     [2, 2, 2],
# ]
# flat = []
# for row in matrix:
#     for num in row:
#         flat.append(num)
#
# flat
# [0, 0, 0, 1, 1, 1, 2, 2, 2]
#
#
# sum the squares of the first one-thousand integers, then a list comprehension
# will solve this problem admirably:
#
#
# sum([i * i for i in range(1000)])
# 332833500
#
#
# The example below uses a generator:
#
#
# sum(i * i for i in range(1000000000))
# 333333332833333333500000000
#
#
# map() also operates lazily, meaning memory won’t be an issue if you choose to use it in this case:
#
#
# sum(map(lambda i: i*i, range(1000000000)))

# 333333332833333333500000000
#
#
# You can use timeit to compare the runtime of map(), for loops, and list comprehensions:
#
#


TAX_RATE = .08
txns = [random.randrange(100) for _ in range(1000000)]


def get_price(txn):
    return txn * (1 + TAX_RATE)


def get_prices_with_map():
    return list(map(get_price, txns))


def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]


def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price(txn))
    return prices


#


print(f"Timer with map: {timeit.timeit(get_prices_with_map, number=100)}")
# 2.0554370979998566
print(f"Timer with comprehension: {timeit.timeit(get_prices_with_comprehension, number=100)}")
# 2.0554370979998566
# 2.3982384680002724
print(f"Timer with loop: {timeit.timeit(get_prices_with_loop, number=100)}")
# 2.0554370979998566
# 3.0531821520007725
