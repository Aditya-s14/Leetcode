class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = 0
        while low<=high:
            mid = (low+high)//2

            tot_hrs = 0
            for pile in piles:
                tot_hrs+=ceil(pile/mid)

            if tot_hrs<=h:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans
        