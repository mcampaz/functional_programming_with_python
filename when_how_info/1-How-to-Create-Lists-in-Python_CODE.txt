If you want to create a list containing the first ten perfect squares, then you can complete these steps in three lines of code:

>>> squares = []
>>> for i in range(10):
...     squares.append(i * i)
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


consider a situation in which you need to calculate the price after tax for a list of transactions:

>>>
>>> txns = [1.09, 23.56, 57.84, 4.56, 6.78]
>>> TAX_RATE = .08
>>> def get_price_with_tax(txn):
...     return txn * (1 + TAX_RATE)
>>> final_prices = map(get_price_with_tax, txns)
>>> list(final_prices)
[1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]


you could rewrite the for loop from the first example in just a single line of code:

>>>
>>> squares = [i * i for i in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


You can rewrite the pricing example with its own list comprehension:

>>>
>>> txns = [1.09, 23.56, 57.84, 4.56, 6.78]
>>> TAX_RATE = .08
>>> def get_price_with_tax(txn):
...     return txn * (1 + TAX_RATE)
>>> final_prices = [get_price_with_tax(i) for i in txns]
>>> final_prices
[1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]