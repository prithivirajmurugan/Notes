import random


def is_sorted(values):
    if len(values) == 1:
        return True
    return values[0] < values[1] and is_sorted(values[1:])


numbers = random.sample(range(0, 1000), 20)
print(numbers)
print(is_sorted(numbers))


def quicksort(values):
    if len(values) <= 1:
        return values
    """
    Pivot is like the centre of see-saw
    """
    pivot = values[0]
    less_than_pivot = []
    greater_than_pivot = []
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


sorted_numbers = quicksort(numbers)
print(sorted_numbers)
print(is_sorted(sorted_numbers))
