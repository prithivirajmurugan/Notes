import random

numbers = random.sample(range(0, 1000000), 10)

print(numbers)


def selection_sort(values):
    """creates a new arry, checks the min
    of the unsorted array one by one and move the minimum
    to sorted array"""
    sorted_list = []
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list


def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index


print("sorted_list")
print(selection_sort(numbers))
