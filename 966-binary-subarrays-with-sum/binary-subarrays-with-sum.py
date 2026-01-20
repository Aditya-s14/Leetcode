class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = {0: 1}   # prefix_sum -> frequency
        prefix = 0
        count = 0

        for num in nums:
            prefix += num

            if prefix - goal in hashmap:
                count += hashmap[prefix - goal]

            hashmap[prefix] = hashmap.get(prefix, 0) + 1

        return count

# since this has 0 we cant use sliding window