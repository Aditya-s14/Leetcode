class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n = start ^ goal
        res= 0
        while n!=0:
            res +=n & 1
            n=n>>1
        return res
        

        