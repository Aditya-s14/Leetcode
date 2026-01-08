class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        res=[]

        for i in range(0,len(nums)):
            difference = target-nums[i]
            if difference in hashmap:
                 res.append(hashmap[difference])
                 res.append(i)
                 return res
            hashmap[nums[i]]=i

            