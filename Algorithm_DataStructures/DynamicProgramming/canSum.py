""" Write a function 'canSum(targetSum,numbers)' that takes in a targetSum
and an array of numbers as arguments.

The function should return a boolean indication whether or not it is possible
to generate the targetSum using numbers from the array

you may use an element of the array as many times as needed.

You may assume that all input numbers are non-negative

example :

canSum[7,[5,3,4,7]] -> true
canSum(7,[2,4]) -> false

"""

# Using recursion
from typing import KeysView


def canSum(targetSum, numbers):
    # base case
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for i in numbers:
        remainder = targetSum - i
        if canSum(remainder, numbers) == True:
            return True
    return False


"""m = target sum and n = array length
   In worstcase the array [1,1,1....], so height of the tree in m
   as we are subtracting 1 from m for each level
   Branching factor is n as at each node of the tree the it branches to n nodes
   hence the O(n^m) - exponential time
   space complexity is height of the tree which is O(m)

"""


def canSum_memo(targetSum, numbers, memo=None):
    if (
        memo is None
    ):  # a mutable argument when added as default argument then the arguement is mutated if the value is mutated.
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for i in numbers:
        remainder = targetSum - i
        if canSum_memo(remainder, numbers, memo):
            memo[targetSum] = True
            return memo[targetSum]
    memo[targetSum] = False
    return False


"""
Time complexity is O(m*n) and Space complexity is O(m)
"""


# print(canSum(7, [5, 3, 4, 7]))
# print(canSum(7, [2, 4]))
# print(canSum(300, [7, 14]))

print(canSum_memo(7, [5, 3, 4, 7]))
print(canSum_memo(7, [2, 4]))
print(canSum_memo(300, [7, 14]))
