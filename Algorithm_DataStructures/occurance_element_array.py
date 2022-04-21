import random


def get_occurance(arr, key):
    count = 0
    for value in arr:
        if value == key:
            count += 1
    return count

numbers = random.sample(range(0, 100), 10)
print(numbers)
print(get_occurance(numbers,3))