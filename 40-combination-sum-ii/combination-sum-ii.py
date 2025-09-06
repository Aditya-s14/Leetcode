class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Step 1: sort to handle duplicates
        subset = []
        def dfs(i,sum):

            #base case:1
            if sum == target:
                res.append(subset.copy())
                return

            #base case:2
            if i>=len(candidates) or sum > target:
                return

            #accept candidates[i]
            subset.append(candidates[i])
            dfs(i+1,sum+candidates[i])

            #reject candidates
            subset.pop()
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:  # to prevent duplicates
                i+=1
            dfs(i+1,sum)

        dfs(0,0)
        return res

            

        