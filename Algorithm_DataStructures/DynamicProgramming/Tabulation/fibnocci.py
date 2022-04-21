"""
Write a function `fib(n)` that takes in a number as an argument. The function should return
n-th number of Fibonacci sequence

The 0th number of the sequence is 0.
The 1st number of the sequence is 1.

"""

def fib(n):
    arr = [0] * (n+2)
    arr[1] = 1
    for i in range(0,n):
        arr[i+1] += arr[i]
        arr[i+2] += arr[i]
    print(arr)
    return arr[n]


print(fib(50))