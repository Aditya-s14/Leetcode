class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 0 #index position for positive values
        j = 1 #index position for negative values
        res = [0]*len(nums)

        for k  in range(len(nums)):
            if nums[k]>0:
                res[i] = nums[k]
                i+=2
            else:
                res[j] = nums[k]
                j+=2
        return res

        