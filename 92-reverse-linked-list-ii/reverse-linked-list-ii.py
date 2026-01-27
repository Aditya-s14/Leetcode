# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        curr = prev.next
        rev_prev = None
        nextnode = None

        for _ in range(right-left+1):
            nextnode = curr.next
            curr.next = rev_prev
            rev_prev = curr
            curr = nextnode

        prev.next.next = curr
        prev.next = rev_prev
    
        return dummy.next