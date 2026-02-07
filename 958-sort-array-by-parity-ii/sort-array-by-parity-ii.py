class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        res = [0]*len(nums)
        for num in nums:
            if num%2 == 0:
                res[i] = num
                i+=2

            else:
                res[j] = num
                j+=2
        return res
            

        