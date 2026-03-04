class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        count = 0
        max_count = 0

        for num in numset:
            if num-1 not in numset:
                count = 1
                while num+count in numset:
                    count+=1
                max_count = max(max_count,count)

        return max_count 
        
        
        
        
        
        
        
        
        
        
        
        """result = 0
        length = 0

        numset = set(nums)

        for num in numset:
            if num-1 not in numset:
                length = 1
                while num+length in numset:
                    length+=1
                result = max(result,length)
            
        return result"""
        