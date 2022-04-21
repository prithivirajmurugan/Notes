# Recursion


def LongestCommonSubSq(str1, str2):
    m = len(str1)
    n = len(str2)
    if 0 in (m, n):
        return 0
    if str1[m - 1] == str2[n - 1]:
        return LongestCommonSubSq(str1[: m - 1], str2[: n - 1]) + 1
    else:
        return max(
            LongestCommonSubSq(str1[: m - 1], str2),
            LongestCommonSubSq(str1, str2[: n - 1]),
        )


print(LongestCommonSubSq("ABCBDAB", "BDCABA"))

# Using dynamic programming
# Top-Down approach


def LongestCommonSubSqDp(str1, str2, memo=None):
    if memo is None:
        memo = {}
    m = len(str1)
    n = len(str2)
    key = (m, n)
    if 0 in key:
        return 0
    if key not in memo:
        if str1[m - 1] == str2[n - 1]:
            result = LongestCommonSubSqDp(str1[: m - 1], str2[: n - 1]) + 1
            memo[key] = result
            return memo[key]
        else:
            result = max(
                LongestCommonSubSq(str1[: m - 1], str2),
                LongestCommonSubSq(str1, str2[: n - 1]),
            )
            memo[key] = result
            return memo[key]


print(LongestCommonSubSqDp("ABCBDAB", "BDCABA"))

# Using tabulation Bottom-up approach


def LongestCommonSubSqTab(str1, str2):
    m = len(str1)
    n = len(str2)

    table = [[0 for i in range(n + 1)] for j in range(m + 1)]

    # The base case table[0][0] is left as zero

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[m][n]


print(LongestCommonSubSqTab("ABCBDAB", "BDCABA"))
print(LongestCommonSubSqTab("zzzzzzzzzzzzzzzzzzzzzzzzzzzzz", "yyyyyyyyyyxxxxxxxxxxxxx"))
