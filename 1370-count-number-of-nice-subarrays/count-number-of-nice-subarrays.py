class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        count = 0
        hashmap = {0:1}
        prefix = 0

        for right in range(len(nums)):
            prefix += nums[right]%2

            if (prefix-k) in hashmap:
                count+=hashmap[prefix-k]

            hashmap[prefix] = hashmap.get(prefix,0)+1

        return count



        