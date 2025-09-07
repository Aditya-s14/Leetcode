class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            # base case: if all chars matched
            if i == len(word):
                return True

            # out of bounds, mismatch, or already visited
            if (r < 0 or c < 0 or r >= rows or c >= columns or
                board[r][c] != word[i] or (r,c) in visited):
                return False

            # choose
            visited.add((r,c))

            # explore
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # unchoose (backtrack)
            visited.remove((r,c))

            return res

        # try starting from each cell
        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True
        return False
