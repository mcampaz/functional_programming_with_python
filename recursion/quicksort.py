import statistics
import random


def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = statistics.median(
            [
                numbers[0],
                numbers[len(numbers) // 2],
                numbers[-1]
            ]
        )
        print(f"Quick_sort -> Input list: {numbers}")
        items_less, pivot_items, items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot]
        )
        print(f"Quick_sort -> Lower list: {items_less}")
        print(f"Quick_sort -> Pivot list: {pivot_items}")
        print(f"Quick_sort -> Higher list: {items_greater}")
        return (
            quicksort(items_less) +
            pivot_items +
            quicksort(items_greater)
        )


def get_random_numbers(length, minimum=1, maximum=100):
    numbers = []
    for _ in range(length):
        numbers.append(random.randint(minimum, maximum))

    return numbers


numbers_to_sort = get_random_numbers(20)
numbers_sorted = quicksort(numbers_to_sort)
print(numbers_sorted)

