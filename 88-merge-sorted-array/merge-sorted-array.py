class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1)-1
        i = m-1 # first element from the right to be non zero in nums1
        j = n-1 # last element of nums2

        while i>=0 and j>=0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i-=1

            else:
                nums1[k] = nums2[j]
                j-=1
            
            k-=1

        # leftover nums2
        while j>=0:
            nums1[k] = nums2[j]
            k-=1
            j-=1
        
        

            

            

        