class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # optimized approach: Boyer–Moore Voting Algorithm

        count,res = 0,0
        for n in nums:
            if count ==0:
                res = n
            
            count+= (1 if res == n else -1)
        
        return res
        
        
        
        
        
        
        
        """hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0)+1
        
        for key,value in hashmap.items():
            if value > len(nums)//2:
                return key"""


