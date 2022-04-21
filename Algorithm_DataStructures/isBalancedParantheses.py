class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            else:
                if stack:
                    x = stack.pop()
                    if not (
                        (x == "[" and s[i] == "]")
                        or (x == "{" and s[i] == "}")
                        or (x == "(" and s[i] == ")")
                    ):
                        return False
                else:
                    return False
            i += 1
        return not stack
