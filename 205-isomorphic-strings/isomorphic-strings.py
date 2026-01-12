class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashmapST,hashmapTS = {},{}

        for i in range(len(s)):
            char_s,char_t = s[i],t[i]

            if (char_s in hashmapST and hashmapST[char_s]!=char_t) or (char_t in hashmapTS and hashmapTS[char_t]!=char_s):
                return False

            hashmapST[char_s] = char_t
            hashmapTS[char_t] = char_s

        return True
        