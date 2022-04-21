def factorial(n):
    res = 500 * [None]
    res_size = 1
    res[0] = 1
    x = 2
    while x <= n:
        res_size = multiply(x, res, res_size)
        print(res_size)
        x = x + 1
    return res[:res_size]


def multiply(x, res, res_size):
    carry = 0
    i = 0
    while i < res_size:
        prod = res[i] * x + carry
        res[i] = prod % 10
        carry = prod // 10
        i = i + 1
    while carry:
        res[res_size] = carry % 10
        carry = carry // 10
        res_size = res_size + 1
    return res_size


arr = factorial(100)
print(arr)
