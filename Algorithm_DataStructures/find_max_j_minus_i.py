def findMaxJMinusI(arr):
    maxDiff = -1
    n=len(arr)
    for i in range(0,n):
       j=n-1
       while(j>i):
           if arr[j]>arr[i] and maxDiff < j-i:
               maxDiff = j-i
           j-=1
    return maxDiff
    
    
arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
n = len(arr)
maxDiff = findMaxJMinusI(arr)
print(maxDiff)