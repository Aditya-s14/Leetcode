class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_set = {}
        for i,num in enumerate(nums):
            diff = target-num
            if diff in index_set:
                return[index_set[diff],i]
            index_set[num] = i
        return False
        