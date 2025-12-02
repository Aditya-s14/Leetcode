class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count  = 1

        #edge case if length of nums is 1 because we need to do this else wont even reach for loop
        if n == 1:
            return True
        
        for i in range(1,n*2):     
            if nums[(i-1)%n] <= nums[i%n]:#do i%n and (i-1)%n to refer back the index position of nums 
                count+=1                  # prevents array index out of bounds
            else:
                count = 1
            
            if count  == n:
                return True
        return False

        