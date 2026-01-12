class Solution:
    def romanToInt(self, s: str) -> int:
        reference_map = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        sum = 0
        i=0
        while i<len(s):
            if i<len(s)-1 and reference_map[s[i]]<reference_map[s[i+1]]:
                sum+=reference_map[s[i+1]]-reference_map[s[i]]
                i+=2
            else:
                sum+=reference_map[s[i]]
                i+=1
        return sum


        