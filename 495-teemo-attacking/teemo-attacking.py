class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        curr = 0
        res = 0
        for t in timeSeries:
            if t>curr:
                res+=duration
            else:
                res += t+duration-curr
            curr = t+duration
        return res