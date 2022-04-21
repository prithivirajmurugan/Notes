def find3Numbers(arr, sum):
    n = len(arr)
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == sum:
                    return arr[i], arr[j], arr[k]
    return -1


def find3NumbersSort(arr, sum):
    arr.sort()
    n = len(arr)
    for i in range(0, n - 2):
        l = i + 1
        r = n - 1
        while l < r:
            if arr[i] + arr[l] + arr[r] == sum:
                return arr[i], arr[l], arr[r]
            elif arr[i] + arr[l] + arr[r] < sum:
                l += 1
            else:
                r -= 1
    return -1


def find3NumbersHash(A, arr_size, sum):
    for i in range(0, arr_size - 1):
        s = set()
        curr_sum = sum - A[i]
        for j in range(i + 1, arr_size):
            if (curr_sum - A[j]) in s:
                return A[i], A[j], curr_sum - A[j]
            s.add(A[j])
        return False
