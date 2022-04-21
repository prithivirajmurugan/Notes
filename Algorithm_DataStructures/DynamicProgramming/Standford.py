def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


print(fact(5))


def sumofn(n):
    if n in (0, 1):
        return n
    return n + sumofn(n - 1)


print(sumofn(5))


def revString(string):
    size = len(string)
    if len(string) == 1:
        return string
    return string[size - 1] + revString(string[: size - 1])


print(revString("Prithiviraj"))


def isPalindrome(string):
    string1 = string.lower()
    size = len(string1)
    if size == 1:
        return True
    return string1[size-1] == string1[0] and isPalindrome(string1[1:size-1])
print(isPalindrome("Malayalam"))

def is_subsequence(needle: str, haystack: str) -> bool:
    if not needle:
        return True
    if not haystack:
        return False
    if needle[0] == haystack[0]:
        return is_subsequence(needle[1:], haystack[1:])
    return is_subsequence(needle, haystack[1:])
print(is_subsequence("hac","cathartic"))

def removeDuplicates(nums):
    k=1
    n=len(nums)
    for i in range(n-1):
        if nums[i]!=nums[i+1]:
            return
    return

