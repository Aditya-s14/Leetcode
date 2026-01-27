# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        while head:
            res = (res<<1)|head.val
            head = head.next

        return res
        
        
        
        """prev = None
        curr = head
        nextnode = None
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        n = 0
        res = 0
        curr = prev
        while curr:
            res += curr.val*(2**n)
            n+=1
            curr = curr.next
        return res"""

        