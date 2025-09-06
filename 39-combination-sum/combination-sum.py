class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, curr_sum):
            # base case: if sum matches target
            if curr_sum == target:
                res.append(subset.copy())
                return
            # base case: if sum exceeds or index out of range
            if i >= len(candidates) or curr_sum > target:
                return

            # include candidates[i]
            subset.append(candidates[i])
            dfs(i, curr_sum + candidates[i])  # we stay at i (reuse same number)

            # exclude candidates[i]
            subset.pop()
            dfs(i + 1, curr_sum)

        dfs(0, 0)
        return res
        