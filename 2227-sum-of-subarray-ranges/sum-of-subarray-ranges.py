class Solution:

    def subArrayMin(self,nums):
        n = len(nums)
        left = [0]*n
        right = [0]*n
        stack=[]

        for i in range(n):
            while stack and nums[i]<nums[stack[-1]]:
                stack.pop()
            left[i] = i-stack[-1] if stack else i+1
            stack.append(i)

        stack.clear()

        for i in range(n-1,-1,-1):
            while stack and nums[i]<=nums[stack[-1]]:
                stack.pop()
            right[i] = stack[-1]-i if stack else n-i
            stack.append(i)

        res = 0
        for i in range(n):
            res = res+left[i]*right[i]*nums[i]
        return res
    
    def subArrayMax(self,nums):
        n = len(nums)
        left = [0]*n
        right = [0]*n
        stack=[]

        for i in range(n):
            while stack and nums[i]>nums[stack[-1]]:
                stack.pop()
            left[i] = i-stack[-1] if stack else i+1
            stack.append(i)

        stack.clear()

        for i in range(n-1,-1,-1):
            while stack and nums[i]>=nums[stack[-1]]:
                stack.pop()
            right[i] = stack[-1]-i if stack else n-i
            stack.append(i)

        res = 0
        for i in range(n):
            res = res+left[i]*right[i]*nums[i]
        return res

    def subArrayRanges(self, nums: List[int]) -> int:
        return (self.subArrayMax(nums) - self.subArrayMin(nums))



        