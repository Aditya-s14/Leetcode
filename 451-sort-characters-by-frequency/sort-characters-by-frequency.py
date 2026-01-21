class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        
        for c in s:
            hashmap[c] = hashmap.get(c,0)+1
        

        hm_sorted = sorted(hashmap.items(),key = lambda x: x[1],reverse = True)
        res = ""
        for i in range(len(hm_sorted)):
            res+=hm_sorted[i][0]*hm_sorted[i][1]
        
        return res




