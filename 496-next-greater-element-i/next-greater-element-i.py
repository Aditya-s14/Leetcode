class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for num in nums1:
            found = False

            for i in range(len(nums2)):
                if nums2[i] == num:
                    j = i + 1
                    while j < len(nums2):
                        if nums2[j] > num:
                            res.append(nums2[j])
                            found = True
                            break
                        j += 1
                    

            if not found:
                res.append(-1)

        return res
