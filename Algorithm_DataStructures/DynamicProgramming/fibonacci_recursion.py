def fibonacci_recursion(n):
    if n <= 2:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

#print(fibonacci_recursion(50)) #will take more than one day to compute

#memoization
#keys will be arg to the fn , value will the be return value
memo = {}

def fibonacci_recursion_memo(n):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    result = fibonacci_recursion_memo(n-1) + fibonacci_recursion_memo(n-2)
    memo[n] = result
    return memo[n]
print(fibonacci_recursion_memo(50))