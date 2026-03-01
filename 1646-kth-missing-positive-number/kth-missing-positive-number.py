class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        return k + high + 1


"""we need to return arr[high]+remaining ------>1
    remaining = k-missing ----> 2
    missing = arr[mid] - (mid + 1) ----->3
    subst 2 with 1
    and put the ans in 1"""

