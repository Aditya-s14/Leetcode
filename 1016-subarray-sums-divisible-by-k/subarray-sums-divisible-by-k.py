class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        prefix = 0
        count = 0

        for num in nums:
            prefix+=num
            rem = prefix%k
            if rem in hashmap:
                count+=hashmap[rem]
            
            hashmap[rem]  = hashmap.get(rem,0)+1
            
        return count