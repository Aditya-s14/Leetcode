class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        #base case, when after recursion through every number in num, the only  number remaining is "nothing"
        if len(nums) ==0:
            return [[]]


        perms = self.permute(nums[1:])   #this is actually the 1st step
        res = []

        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i,nums[0])
                res.append(perm_copy)
        return res
        