def subArrayExists(arr):
    n = len(arr)
    mapped_array = set()
    n_sum = 0
    for i in range(n):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in mapped_array:
            return True
        mapped_array.add(n_sum)
    return False


print(subArrayExists([4, 2, -3, 1, 6]))
print(subArrayExists([-3, 2, 3, 1, 6]))
