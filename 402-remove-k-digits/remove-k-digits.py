class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for curr in num:
            while k > 0 and stack and stack[-1] > curr:
                stack.pop()
                k -= 1
            stack.append(curr)

        # If removals still left, remove from the end
        while k > 0 and stack:
            stack.pop()
            k -= 1

        # Remove leading zeros
        res = "".join(stack).lstrip("0")
        return res if res else "0"
