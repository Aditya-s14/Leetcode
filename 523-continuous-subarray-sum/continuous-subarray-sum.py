class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        hashmap = {0: -1}   # remainder -> earliest index
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]          
            rem = prefix % k           # remainder

            if rem in hashmap:
                if i - hashmap[rem] >= 2:
                    return True
            else:
                hashmap[rem] = i       # store rem not prefix

        return False
