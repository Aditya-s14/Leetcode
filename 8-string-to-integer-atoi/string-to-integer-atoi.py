class Solution:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    def helper(self, s, i, num, sign):
        # Base case
        if i >= len(s) or not s[i].isdigit():
            return sign * num

        # Build number
        num = num * 10 + int(s[i])

        # Handle overflow
        if sign * num <= self.INT_MIN:
            return self.INT_MIN
        if sign * num >= self.INT_MAX:
            return self.INT_MAX

        # Recursive call
        return self.helper(s, i + 1, num, sign)

    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # Skip spaces
        while i < n and s[i] == " ":
            i += 1

        # Handle sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Call helper
        return self.helper(s, i, 0, sign)
