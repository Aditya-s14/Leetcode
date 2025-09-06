class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i>=len(nums):        # base case
                res.append(subset.copy())
                return       # dont forget to exit once all the no parsed
            
            # include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            #exclude nums[i]
            subset.pop()
            dfs(i+1)
        

        dfs(0)
        return res
        