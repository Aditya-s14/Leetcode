class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # lemme create a hashmap that stores element:frequency
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        

        # lemme create a bucket for each frequency 
        # 0  1  2  3  4  5  6. <--- frequency
        #[] [] [] [] [] []  [] <---- bucket
        #nlen = len(nums) <-- instead of this find max frequency from hashmap and create buckets
        # Find the maximum frequency
        max_freq = max(hashmap.values())
        #buckets = [[] for _ in range(nlen+1)]
        buckets = [[] for _ in range(max_freq + 1)]
        

        # now we have to store element inside the [] corresponding to its frequency
        for element,frequency in hashmap.items():
            buckets[frequency].append(element)
        
        # since its top K elements, lets start from right end
        result = []
        for bucket in buckets[::-1]:
            result.extend(bucket)
            if len(result) == k:
                return result


    

        