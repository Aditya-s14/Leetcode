class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0)+1
        
        for key,value in hashmap.items():
            if value > len(nums)//2:
                return key


