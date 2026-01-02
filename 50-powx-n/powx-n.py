class Solution:
    def helper(self, x, n):
        # base case
        if n == 0:
            return 1
        if n == 1:
            return x
        
        if n % 2 == 0:    # if power is even
            return self.helper(x * x, n // 2)
        else:             # if power is odd
            return x * self.helper(x, n - 1)

    def myPow(self, x: float, n: int) -> float:
        # if power is negative: x^-n = 1 / x^n
        if n < 0:
            x = 1 / x
            n = -n

        return self.helper(x, n)
