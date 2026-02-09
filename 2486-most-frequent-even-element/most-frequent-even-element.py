class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hashmap = {}#val:freq

        for num in nums:
            if num%2 == 0:
                hashmap[num] = hashmap.get(num,0)+1

        max_freq = -1 
        res = -1

        for num,freq in hashmap.items():
            if freq>max_freq or (freq == max_freq and num < res):
                max_freq = freq
                res = num

        return res





        