class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0

        for n in range(1,n+1):
            if n%3 == 0 or n%5 == 0 or n%7 ==0:
                sum+=n
        return sum


        