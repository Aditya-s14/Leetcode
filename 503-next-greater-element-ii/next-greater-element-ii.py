class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        
        for i in range(n*2):
            curr  = nums[i%n]

            while stack and curr > nums[stack[-1]]:
                idx=stack.pop()
                res[idx] = curr
            if i<n: 
                stack.append(i)
        return res
        