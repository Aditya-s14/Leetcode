class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffToIdx = {}
        diff = 0
        for i,n in enumerate(nums):
            diff = target-n
            if diff not in diffToIdx:
                diffToIdx[n] = i
            elif diff in diffToIdx:
                return [diffToIdx[diff],i]