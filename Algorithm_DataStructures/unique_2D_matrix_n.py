MAX = 100
arr = [[0 for x in range(MAX)] for y in range(MAX)]


def constructMatrix(n):
    right = n - 1
    left = 0
    for i in range(n):
        if i % 2 == 0:
            arr[i][right] = 1
            fillRemaining(i, right, n)
            right -= 1
        else:
            arr[i][left] = 1
            fillRemaining(i, left, n)
            left += 1


def fillRemaining(i, j, n):
    x = 2
    for k in range(i + 1, n):
        arr[k][j] = x
        x += 1
    for k in range(i):
        arr[k][j] = x
        x += 1


constructMatrix(5)
for i in range(5):
    for j in range(5):
        print(arr[i][j], end=" ")
    print("")
