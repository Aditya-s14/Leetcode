
class Solution:
    """
        Do not return anything, modify nums in-place instead.
    """
    """
        rotating an array right by k elements mean taking the last k elements and placing in the front
        rotating an array left by k elements mean taking the first k elements and placing in the last
    """
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
