def getMinDiff(arr, n, k):
    arr.sort()
    ans = arr[n - 1] - arr[0]
    small, big = 0, 0
    for i in range(1, n):
        small = min(arr[0] + k, arr[i] - k)  # finding the minimum tower height
        big = max(arr[i - 1] + k, arr[-1] - k)  # finding maximum tower height
        ans = min(ans, big - small)
        return ans


arr = [1, 10, 14, 14, 14, 15]
k = 6
print(getMinDiff(arr, len(arr), k))
