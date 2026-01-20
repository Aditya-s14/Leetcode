class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        hashmap = {0:-1}
        prefix = 0
        maxlen = 0
        for i in range(len(nums)):
            prefix+=nums[i]
            rem = prefix%k
            if rem in hashmap:
                maxlen = max(maxlen,i-hashmap[rem])
            
            if rem not in hashmap:
                hashmap[rem] = i
            
        return (maxlen>=2)

        