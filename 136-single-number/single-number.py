class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # default value has been given as 0 because n^0 = n
        for n in nums:
            res ^=n
        return res