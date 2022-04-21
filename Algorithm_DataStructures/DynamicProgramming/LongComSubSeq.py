def LongCommonSubSeqLength(str1, str2):
    m = len(str1)
    n = len(str2)
    table = [[0 for x in range(n + 1)] for y in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table


def LongCommonSubSeq(str1, str2, m, n, table=None):
    if m == 0 or n == 0:
        return str()
    if table is None:
        table = LongCommonSubSeqLength(str1, str2)
        print(table)
    if str1[m - 1] == str2[n - 1]:
        return LongCommonSubSeq(str1, str2, m - 1, n - 1, table) + str1[m-1]
    if table[m - 1][n] > table[m][n - 1]:
        return LongCommonSubSeq(str1, str2, m - 1, n, table)
    return LongCommonSubSeq(str1, str2, m, n - 1, table)


X = "XMJYAUZ"
Y = "MZJAWXU"

m = len(X)
n = len(Y)
# find the longest common sequence
print(LongCommonSubSeq(X, Y, m, n))
