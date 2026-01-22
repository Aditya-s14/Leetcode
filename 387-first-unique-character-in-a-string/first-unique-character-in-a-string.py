class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}#char:count
        for c in s:
            hashmap[c] = hashmap.get(c,0)+1

        for char,count in hashmap.items():
            if count ==1:
                for i in range(len(s)):
                    if char == s[i]:
                        return i
        return -1
        