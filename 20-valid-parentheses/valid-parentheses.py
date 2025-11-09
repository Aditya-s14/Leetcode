class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack or d[i]!=stack[-1]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False