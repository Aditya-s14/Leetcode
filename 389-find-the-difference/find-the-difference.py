class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0

        for c in s+t:
            char = ord(c)
            res^=char

        return chr(res)







        