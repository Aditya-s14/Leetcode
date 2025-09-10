class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case: if both their lengths are equal or not 
        if len(s)!=len(t):
            return False

        #create hash map for both the strings
        map_s , map_t = {},{}

        for i in range(len(s)):
            map_s[s[i]] = 1+ map_s.get(s[i],0)
            # get is to check only if that string is there in map_S
            map_t[t[i]] = 1 + map_t.get(t[i],0)

        for c in map_s:
            if map_s[c] != map_t.get(c,0):
                return False
        return True


