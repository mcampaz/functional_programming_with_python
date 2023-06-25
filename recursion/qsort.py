# qsort.py
from statistics import median

def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = median([numbers[0], numbers[len(numbers) // 2], numbers[-1]])
    smaller = []
    same = []
    larger = []
    for num in numbers:
        if num < pivot:
            smaller.append(num)
        elif num > pivot:
            larger.append(num)
        else:
            same.append(num)

    return quicksort(smaller) + same + quicksort(larger)



def p_quicksort(numbers):
    print(f"quicksort({numbers})")
    if len(numbers) <= 1:
        print("  returning", numbers)
        return numbers

    pivot = median([numbers[0], numbers[len(numbers) // 2], numbers[-1]])
    print("  pivot:", pivot)
    smaller = []
    same = []
    larger = []
    for num in numbers:
        if num < pivot:
            smaller.append(num)
        elif num > pivot:
            larger.append(num)
        else:
            same.append(num)

    print("  lists:")
    print("     smaller:", smaller)
    print("        same:", same)
    print("      larger:", larger)
    return p_quicksort(smaller) + same + p_quicksort(larger)
