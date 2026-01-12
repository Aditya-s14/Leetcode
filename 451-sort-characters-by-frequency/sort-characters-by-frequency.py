class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i],0)+1
        
        hashmap_list = list(hashmap.items())

        hashmap_list.sort(key = lambda x: x[1],reverse = True)
        res = ""
        for char,count in hashmap_list:
            res+=char*count
        
        return res




