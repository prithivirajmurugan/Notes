import random


def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[0]
    left_array = []
    right_array = []
    for value in arr[1:]:
        if value <= pivot:
            left_array.append(value)
        else:
            right_array.append(value)
    return quick_sort(left_array) + [pivot] + quick_sort(right_array)


def get_k_smallest_element(sorted_arr, k):
    return sorted_arr[k - 1]


def get_k_largest_element(sorted_arr, k):
    n = len(sorted_arr)
    i = n - k
    return sorted_arr[i]


numbers = random.sample(range(0, 10), 10)
print(numbers)
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)
print(get_k_smallest_element(sorted_numbers,3))
print(get_k_largest_element(sorted_numbers,3))
