from collections import defaultdict


def firstNonRepeatingEff(arr):
    n = len(arr)
    map_array = defaultdict(lambda: 0)
    for i in range(n):
        map_array[arr[i]] += 1
    for i in range(n):
        if map_array[arr[i]] == 1:
            return arr[i]
    return -1


def firstNonRepeating(arr):
    n = len(arr)
    for i in range(n):
        j = 0
        while j < n:
            if i != j and arr[i] == arr[j]:
                break
            j += 1
        if j == n:
            return arr[i]
    return -1


def firstNonRepeatingSet(arr):

    # Insert all array elements in hash
    # table
    n = len(arr)
    mp = {}
    for i in range(n):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        mp[arr[i]] += 1

    # Traverse through map only and
    for x in mp:
        if mp[x] == 1:
            print(x, end=" ")


arr = [9, 4, 9, 6, 7, 4]
n = len(arr)
print(firstNonRepeating(arr))
print(firstNonRepeatingEff(arr))
firstNonRepeatingSet(arr)
