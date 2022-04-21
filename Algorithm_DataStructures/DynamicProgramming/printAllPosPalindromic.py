def isPalidrome(low, high, str):
    while low < high:
        if str[low] != str[high]:
            return False
        low += 1
        high -= 1
        return True


def IsPalindrome_recur(string):
    size = len(string)
    if size == 0 or size == 1:
        return True
    return string[0] == string[size-1] and IsPalindrome_recur(string[1 : size - 1])


print(IsPalindrome_recur("malayalam"))
