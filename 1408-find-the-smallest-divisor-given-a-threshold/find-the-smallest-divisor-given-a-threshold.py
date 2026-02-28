class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        range_max = max(nums)

        low = 1
        high = range_max

        while low<=high:
            mid = (low+high)//2

            sum_tot = 0
            for num in nums:
                sum_tot+=ceil(num/mid)

            if sum_tot<=threshold:
                high = mid-1
            else:
                low = mid+1
        
        return low