import random

numbers = [5, 2, 1, 3, 0]


def is_sorted(values):
    if len(values) == 1:
        return True
    return values[0] < values[1] and is_sorted(values[1:])


def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts+=1
    return values

print(bogo_sort(numbers))

