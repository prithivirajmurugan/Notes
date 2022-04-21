def printSpiralMatrix(arr):
    result = []
    if arr == []:
        return result
    top = 0
    bottom = len(arr)
    left = 0
    right = len(arr[0])
    size = bottom * right
    while len(result) < size:
        i = left
        while i <= right and len(result) < size:
            result.append(arr[top][i])
            i += 1
        top += 1
        i = top
        while i >= bottom and len(result) < size:
            result.append(arr[i][right])
            i -= 1
        right -= 1
        i = right
        while i >= left and len(result) < size:
            result.append(arr[bottom][i])
            i -= 1
        bottom -= 1
        i = bottom
        while i <= top and len(result) < size:
            result.append(arr[i][left])
            i += 1
        left += 1
    return result


a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print(printSpiralMatrix(a))
