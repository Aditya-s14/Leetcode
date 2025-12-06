class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxsum = float('-inf')

        for n in nums:
            sum+=n
            maxsum = max(sum,maxsum)

            if sum<0:
                sum = 0
            
        return maxsum
        