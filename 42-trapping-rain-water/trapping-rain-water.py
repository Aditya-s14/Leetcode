class Solution:
    def prefix(self,nums):
        n = len(nums)
        p_res = [0]*n
        p_res[0] = nums[0]
        for i in range(1,len(nums)):
            p_res[i] = max(nums[i],p_res[i-1])
        return p_res
    
    def suffix(self,nums):
        n = len(nums)
        s_res = [0]*n
        s_res[n-1] = nums[-1]
        for i in range(n-2,-1,-1):
            s_res[i] = max(nums[i],s_res[i+1])
        return s_res

    def trap(self, height: List[int]) -> int:
        total = 0
        leftmax = self.prefix(height)
        rightmax = self.suffix(height)
        for i in range(len(height)):
            total += min(leftmax[i],rightmax[i]) - height[i]
        return total

