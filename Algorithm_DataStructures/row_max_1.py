def Binary_search(arr, low, high):
    if high >= low:
        mid = (low + high) // 2
        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
            return mid
        elif arr[mid] == 0:
            return Binary_search(arr, mid + 1, high)
        else:
            return Binary_search(arr, low, (mid - 1))
    return -1

def rowWithMax1s(arr):
    R = len(arr)
    C = len(arr[0])
    max_row_index = 0
    max = -1

    for i in range(0,R):
        index = Binary_search(mat[i],0,C-1)
        if index != -1 and C-index > max: 
            max = C-index
            max_row_index = i
    return max_row_index

mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print ("Index of row with maximum 1s is",
      rowWithMax1s(mat))
