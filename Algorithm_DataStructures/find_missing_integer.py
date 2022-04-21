def get_missing(arr):
    n = len(arr)
    for i, val in enumerate(arr):
        if i + 1 != val:
            return i + 1
    return None

numbers = [1,2,3,4,5]
print(get_missing(numbers))
