class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        prefix = 0
        count = 0
        for num in nums:
            prefix+=num

            if prefix-k in hashmap:   # prefix[j]-prefix[i] = k
                count+=hashmap[prefix-k]
            
            hashmap[prefix] = hashmap.get(prefix,0)+1
            
        return count
            

        