class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Truncate toward zero
        res = int(dividend / divisor)

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX

        return res
