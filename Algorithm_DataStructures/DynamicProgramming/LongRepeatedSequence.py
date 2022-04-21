def LRSLength(X,m,n):
    if m==0 or n==0:
        return 0
    if X[m-1] == X[n-1] and m!=n:
        return LRSLength(X,m-1,n-1) + 1
    return max(LRSLength(X,m-1,n), LRSLength(X,m,n-1))

X = "ATACTCGGA"
m = len(X)
print(LRSLength(X,m,m))

def LRSLength_memo(X,m,n,memo=None):
    if memo == None:
        memo={}
    if m==0 or n==0:
        return 0
    key = (m,n)
    if key in memo:
        return memo[key]
    if X[m-1] == X[n-1] and m!=n:
        memo[key] = LRSLength_memo(X,m-1,n-1,memo) + 1
        return memo[key]
    memo[key] = max(LRSLength_memo(X,m-1,n,memo),LRSLength_memo(X,m,n-1,memo))
    return memo[key]

X = "ATACTCGGA"
m = len(X)
print(LRSLength_memo(X,m,m))

def LRSLength_DP(X,m):
    T = [[0 for x in range(m+1)]for y in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,m+1):
            if X[i-1] == X[j-1] and i!=j:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i][j-1],T[i-1][j])
    return T[m][m]
X = "ATACTCGGA"
m = len(X)
print(LRSLength_DP(X,m))