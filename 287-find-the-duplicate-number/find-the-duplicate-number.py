class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow] # similar to slow = slow.next
            fast = nums[nums[fast]] # similar to fast = fast.next.next

            if slow == fast:
                break
        
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
