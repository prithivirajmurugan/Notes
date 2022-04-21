# kadane's algorithm


def largest_sum_max_index(arr):
    max_so_far = max_ending_here = 0
    n = len(arr)
    for i in range(n):
        max_ending_here += arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far


print(largest_sum_max_index([-2, -3, 4, -1, -2, 1, 5, -3]))
