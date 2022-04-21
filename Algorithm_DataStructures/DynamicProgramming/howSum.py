"""
Write a function `howSum(targetSum,numbers)` that takes in a targetSum and
an array of numbers as arguments.

The function should return an array containing any combination of elements
that add up to exactly the targetSum. If there is no combination that adds
up to the targetSum, then return null

If there are multiple combinations possible, you may return any single one

"""

def howSum(targetSum,numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for number in numbers:
        remainder = targetSum - number
        remainder_result = howSum(remainder,numbers)
        if remainder_result!=None:
            combination = [*remainder_result,number] # python spread operator
            return combination
    return None

# m is targetSum and n = len(numbers)
# Time complexity = O(n^m * m)
# Space complexity = O(m)

def howSumMemo(targetSum,numbers,memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for number in numbers:
        remainder = targetSum - number
        remainder_result = howSumMemo(remainder,numbers,memo)
        if remainder_result!=None:
            combination = [*remainder_result,number] # python spread operator
            memo[targetSum] = combination
            return memo[targetSum]
    memo[targetSum] = None
    return None
"""
Time : O(n*m*m)
Space complexity : O(m*m)
"""
print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSumMemo(300,[7,14])) # wont work in usual recursion
print(howSumMemo(300,[7,10,14])) # wont work in usual recursion
print(howSumMemo(300,[1,1])) # wont work in usual recursion    
