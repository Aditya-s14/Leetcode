class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = 1 if x >= 0 else -1
        x = abs(x)

        new = 0
        while x != 0:
            rem = x % 10
            x //= 10
            new = new * 10 + rem

        new *= sign

        if new < INT_MIN or new > INT_MAX:
            return 0

        return new