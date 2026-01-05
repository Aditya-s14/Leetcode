class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, open_cnt, close_cnt):
            # base case
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # add "("
            if open_cnt < n:
                backtrack(curr + "(", open_cnt + 1, close_cnt)

            # add ")"
            if close_cnt < open_cnt:
                backtrack(curr + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return res
