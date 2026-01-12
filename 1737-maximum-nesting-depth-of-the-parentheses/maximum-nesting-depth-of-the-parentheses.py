class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxdepth = 0
        for char in s:
            if char == '(':
                depth+=1
                maxdepth = max(depth,maxdepth)
            elif char == ')':
                depth-=1
            else:
                continue
        return maxdepth

        