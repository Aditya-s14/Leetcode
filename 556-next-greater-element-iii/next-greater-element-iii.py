class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        length = len(nums)

        # Step 1: find pivot
        i = length - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            return -1

        # Step 2: find next greater element
        j = length - 1
        while nums[j] <= nums[i]:
            j -= 1

        # Step 3: swap
        nums[i], nums[j] = nums[j], nums[i]

        # Step 4: reverse suffix
        nums[i + 1:] = reversed(nums[i + 1:])

        res = int("".join(nums))
        return res if res <= 2**31 - 1 else -1
