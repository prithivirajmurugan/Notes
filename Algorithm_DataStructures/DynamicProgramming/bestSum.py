"""Write a function `bestSum(targetSum,numbers)` that takes in a targetSum and an array of numbers as
arguements.

The function should return an array containing the shortest combination of numbers that add up to exactly
the targetSum

If there is a tie for the shortest combination, you can return any on of the shortest.
"""


def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortest_combination = None
    for number in numbers:
        remainder = targetSum - number
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination is not None:
            combination = [*remainderCombination, number]
            if shortest_combination is None or len(combination) < len(
                shortest_combination
            ):
                shortest_combination = combination
    return shortest_combination


"""
m - targetSum
n - numbers.length

Time : O(n^m * m)

Space : O(m*m) - maximum stack depth is still m, but every recursive call
will save m length array

"""


def bestSum_memo(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortest_combination = None
    for number in numbers:
        remainder = targetSum - number
        remainderCombination = bestSum_memo(remainder, numbers, memo)
        if remainderCombination is not None:
            combination = [*remainderCombination, number]
            if shortest_combination is None or len(shortest_combination) > len(
                combination
            ):
                shortest_combination = combination
    memo[targetSum] = shortest_combination
    return shortest_combination


"""
time = O(n*m*m)
space complexity = O(m*m)
"""

print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(8, [1, 4, 5]))
print(bestSum_memo(100, [1, 2, 5, 25]))

"""
Dynamic programming problems are
Decision problem
Combinatoric problem
Optimization problem
"""
