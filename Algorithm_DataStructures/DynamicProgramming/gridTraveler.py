"""Say that you are traveler on a 2D grid . You begin in the top left corner and your goal
your goal is to travel to the bottom-right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m*n?

Write a function `gridTraveler(m,n)` that calculates this"""

memo = {}


def gridTraveler(m, n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)


def gridTraveler_memo(m, n):
    key = str(m) + "," + str(n)
    if key in memo:
        return memo[key]
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        result = gridTraveler_memo(m - 1, n) + gridTraveler_memo(m, n - 1)
        memo[key] = result
    return memo[key]


# no of ways to travel a (1,n) is same as the number of ways to travel a (n,1), hence(n,m) = (m,n)

# memoized time complexity is O(m*n) because there are always m*n combination of m and n and space complexity is O(n+m)
print(gridTraveler_memo(18, 18))

"""Memmoization Recipe

1. Make in work - using recursion
    1. visualize the problem as a tree
    2. implement the tree using recursion - leaf is the base case
    3. test it
2. Make in efficient
    1. add a memo object
    2. add a base case to return memo values
    3. store return values into the memo
"""
