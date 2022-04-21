from typing import ForwardRef


import random


def get_reversed_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


numbers = random.sample(range(10), 10)
print(numbers)
get_reversed_array(numbers)
print(numbers)
