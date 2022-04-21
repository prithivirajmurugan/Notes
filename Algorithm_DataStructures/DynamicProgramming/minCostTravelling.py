"""
Optimal substructure problem can be solved using dynamic programming

There is a problem of overlapping subproblem, which takes the time complexity to exponential time and memory

The Time complexity of recursion is always equal to the number of branches each branch can give rise or number of recursive call at each branch
to the power of cost we are trying to solve.

Memoization store the value of result when it is calculated once, there will two types of calls in memoized function
1. memoized calls -> already solved and takes O(1) constant time
2. non-memoized calls -> there will be exactly O(n) calls

Memoization = Recursion + Cache - Recomputing overlapping subproblems
"""


def minCostTravelling(s, d, cost):
    if s == d or s + 1 == d:
        return cost[s][d]
    minCost = cost[s][d]
    for i in range(s + 1, d):
        temp_cost = minCostTravelling(s, i, cost) + minCostTravelling(i, d, cost)
        minCost = min(temp_cost, minCost)
    return minCost
"""Using Dynamic Programming bottom-up approach"""
def minCostTravellingwithDP(cost):
    size = len(cost)
    min = [0 for i in range(size+1)]
    min[0]=0
    min[1]=cost[0][1]
    for i in range(2,size):
        min[i] = cost[0][i]
        for j in range(0,i):
            if(min[i]>min[j]+cost[j][i]):
                min[i] = min[j] + cost[j][i]
    return min[size]




cost = [[0, 50, 80, 50], [-1, 0, 50, 20], [-1, -1, 0, 20], [-1, -1, -1, 0]]
print(minCostTravelling(0, 3, cost))

print(minCostTravellingwithDP(cost))

