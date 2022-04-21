def LongCommonSubSequenceLength(str1,str2):
    m = len(str1)
    n = len(str2)
    table = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j],table[i][j-1])
    return table

def diff(X,Y,m,n,table=None):
    if table is None:
        table = LongCommonSubSequenceLength(X,Y)
    if m>0 and n>0 and X[m-1]==Y[n-1]:
        diff(X,Y,m-1,n-1,table)
        print("", X[m - 1], end='')
    elif n>0 and (m==0 or table[m][n-1]>=table[m-1][n]):
        diff(X,Y,m,n-1,table)
        print(" +" + Y[n-1],end='')
    elif m>0 and (n==0 or table[m][n-1]<table[m-1][n]):
        diff(X,Y,m-1,n,table)
        print(' -' + X[m-1],end='')

X = "ABCDFGHJQZ"
Y = "ABCDEFGIJKRXYZ"
diff(X, Y, len(X), len(Y))
 