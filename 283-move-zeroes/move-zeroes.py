class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0  # pointer to place next non-zero

        for right in range(1, len(nums)):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
            
            # if nums[left] is non-zero, move left forward
            if nums[left] != 0:
                left += 1
