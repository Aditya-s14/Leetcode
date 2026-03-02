class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0  # pointer to place next non-zero
        """while right<len(nums):
            if nums[right]!=0:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right+=1
            else:
                right+=1"""
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1

            


