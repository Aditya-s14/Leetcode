class Solution:
 def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    
    # PASS 1: Walk left to right
    # Record: "What numbers did I pass BEFORE arriving here?"
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix        # What I passed before
        prefix *= nums[i]      # Now I'm passing this number
    
    # PASS 2: Walk right to left
    # Multiply: "What numbers did I pass BEFORE arriving here?"
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix      # Multiply with what I passed before
        postfix *= nums[i]     # Now I'm passing this number
    
    return res
        